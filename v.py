import fitz  # PyMuPDF
import re
import json
import faiss
import numpy as np
import torch
from transformers import MarianMTModel, MarianTokenizer, AutoTokenizer, AutoModel

# -----------------------------
# PDF 읽기
def get_pdf_text(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# -----------------------------
# 문장 단위 분리 후 900자 기준 청크
def split_into_chunks(text, max_chunk_len=900):
    sentences = re.split(r'(?<=[.?!])\s+', text)
    chunks = []
    current_chunk = ""
    for s in sentences:
        if len(current_chunk) + len(s) <= max_chunk_len:
            current_chunk += s + " "
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = s + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# -----------------------------
# Marian 번역 모델 (한국어 → 영어)
TRANS_PATH = "./trans/ko-en"
tokenizer_trans = MarianTokenizer.from_pretrained(TRANS_PATH)
model_trans = MarianMTModel.from_pretrained(TRANS_PATH)

'''
def translate_en(text):
    tokens = tokenizer_trans(text, return_tensors="pt", padding=True)
    with torch.no_grad():
        generated_ids = model_trans.generate(**tokens)
    return tokenizer_trans.decode(generated_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

'''


import re

def translate_en(text):
    # 1. 문장 단위로 분리 (.?! 기준, 공백 포함)
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    translations = []

    # 2. 각 문장을 개별 번역
    for sent in sentences:
        if sent.strip():  # 빈 문장은 무시
            tokens = tokenizer_trans(sent, return_tensors="pt", padding=True)
            with torch.no_grad():
                generated_ids = model_trans.generate(**tokens)
            translated = tokenizer_trans.decode(
                generated_ids[0], 
                skip_special_tokens=True, 
                clean_up_tokenization_spaces=True
            )
            translations.append(translated)

    # 3. 결과 합치기 (문장 사이에 공백 추가)
    return " ".join(translations)















# -----------------------------
# Ko-SRoBERTa 임베딩 모델
tokenizer_embed = AutoTokenizer.from_pretrained("./ko-sroberta-multitask")
model_embed = AutoModel.from_pretrained("./ko-sroberta-multitask")
model_embed.eval()

def get_chunk_embedding(text):
    inputs = tokenizer_embed(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model_embed(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :]
    return cls_embedding.squeeze().numpy()

# -----------------------------
# PDF 처리
pdf_text = get_pdf_text("./건강보험자료.pdf")
print('학습 자료 입력')

# 문장 단위로 청크 생성
korean_chunks = split_into_chunks(pdf_text, max_chunk_len=300)
print('청크 분리 완료 (청크 당 300자 이내)')

i = 1
for item in korean_chunks:
    print(i)
    i += 1
    print(item)
    print()

# 각 청크를 영어로 번역
# english_chunks = [translate_en(chunk) for chunk in korean_chunks]


english_chunks = []
for i, chunk in enumerate(korean_chunks):
    eng_chunk = translate_en(chunk)
    english_chunks.append(eng_chunk)
    print(f"청크 {i+1} 번역 완료: {eng_chunk[:].replace('\n', ' ')} ... [{len(eng_chunk)} 글자]")
    print()



print('청크 영어 번역 완료')
print(english_chunks[0])
print()
print(str(len(english_chunks)) + ' 개 청크')
print()


# -----------------------------
# 청크 미리보기 출력
print("\n[청크 미리보기]")
for i, chunk in enumerate(korean_chunks):
    # 숫자/기호 카운트
    if sum(ch.isdigit() or ch in '()[], .' for ch in chunk[:30]) < 7:
        print(f"청크 {i+1}: {chunk[:30].replace('\n', '')} ...\t[{len(chunk)}글자]")
    else:
        print(f"청크 {i+1}: {chunk[:30].replace('\n', '')} ...\t\t[{len(chunk)}글자]")
print()

# -----------------------------
# 청크 임베딩
chunk_embeddings = [get_chunk_embedding(chunk) for chunk in english_chunks]  # 영어 청크 벡터

# -----------------------------
# 벡터 DB
embedding_dim = chunk_embeddings[0].shape[0]  # 첫 번째 벡터 차원
index = faiss.IndexFlatL2(embedding_dim)
index.add(np.array(chunk_embeddings))

# -----------------------------
# 첫 번째 청크 토큰 임베딩 확인
inputs = tokenizer_embed(english_chunks[0], return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    outputs = model_embed(**inputs)

token_vectors = outputs.last_hidden_state.squeeze(0)  # (토큰 수, 768)
tokens = tokenizer_embed.convert_ids_to_tokens(inputs['input_ids'][0])

print(f"\n청크1: {korean_chunks[0][:30].replace(chr(10), '')} ... \t[{len(korean_chunks[0])}글자]\n")
for i in range(min(8, len(tokens))):
    if len(tokens[i]) < 2:
        print(f"토큰{i+1} {tokens[i]}\t\t", str(token_vectors[i][:5].numpy()).replace(']', ' ... ➝ 768 차원 ]'))
    else:
        print(f"토큰{i+1} {tokens[i]}\t", str(token_vectors[i][:5].numpy()).replace(']', ' ... ➝ 768 차원 ]'))

# -----------------------------
# FAISS와 청크 저장
faiss.write_index(index, "vector_index.faiss")
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(english_chunks, f, ensure_ascii=False)

print(f"\n총 {len(english_chunks)}개의 청크 생성 및 FAISS 인덱스 저장 완료.")
