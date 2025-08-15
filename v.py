


from transformers import AutoTokenizer, AutoModel
import torch
import fitz  # PyMuPDF
import json
import faiss
import numpy as np





import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"





def get_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def get_chunk(text, chunk_size=900, overlap=200):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        if end > text_length:
            end = text_length
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap  # 겹치는 부분 유지하며 이동

    return chunks


def get_chunk_embeddings(chunk):
    inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :]  # [CLS] 토큰
    return cls_embedding.squeeze().numpy()






tokenizer = AutoTokenizer.from_pretrained("./ko-sroberta-multitask")
model = AutoModel.from_pretrained("./ko-sroberta-multitask")
model.eval()







# 시작
text = ''
text += get_pdf(".\건강보험자료.pdf")
chunks = get_chunk(text, chunk_size=300, overlap=50)   # 청크 구분

for i, chunk in enumerate(chunks):
    if sum(ch.isdigit() or ch in '()[], .' for ch in chunk[:30]) < 7:
        print(f"청크 {i+1}: {chunk[:30].replace('\n', '')} ...\t[{len(chunk)}글자]")
    else:
        print(f"청크 {i+1}: {chunk[:30].replace('\n', '')} ...\t\t[{len(chunk)}글자]")

print()


# 청크 임베딩
chunk_embeddings = [get_chunk_embeddings(chunk) for chunk in chunks]   # 청크 벡터 (10개 청크의 768 벡터들)


# 벡터DB
# 유사도 검색 준비
embedding_dim = chunk_embeddings[0].shape[0]    # 첫 번째 임베딩 벡터의 차원(벡터 길이)을 구함
index = faiss.IndexFlatL2(embedding_dim)        # L2 거리(유클리디안 거리) 기준 인덱스 생성
index.add(np.array(chunk_embeddings))           # 임베딩 벡터들을 numpy 배열로 변환해 인덱스에 추가

inputs = tokenizer(chunks[0], return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)

token_vectors = outputs.last_hidden_state.squeeze(0)  # (토큰수, 768)
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])


print('청크1: ' + chunks[0][:30].replace('\n', '') + ' ... \t[' + str(len(chunks[0])) + '글자]')

for i in range(8):
    if len(tokens[i]) < 2:
        print(f"토큰{i+1} {tokens[i]}\t\t", str(token_vectors[i][:5].numpy()).replace(']', ' ... ➝  768 차원 ]'))
    else:
        print(f"토큰{i+1} {tokens[i]}\t", str(token_vectors[i][:5].numpy()).replace(']', ' ... ➝  768 차원 ]'))

print()


faiss.write_index(index, "vector_index.faiss")   # faiss 저장 (벡터 인덱스)
with open("chunks.json", "w", encoding="utf-8") as f:   # 청크 JSON 파일 저장
    json.dump(chunks, f, ensure_ascii=False)

















index = faiss.read_index("vector_index.faiss")

with open("chunks.json", "r", encoding="utf-8") as f:   # faiss의 청크를 chunks 에 저장
    chunks = json.load(f)

for i, chunk in enumerate(chunks): # 청크 출력
    if sum(ch.isdigit() or ch in '()[], .' for ch in chunk[:30]) < 7:
        print(f"청크 {i+1}: {chunk[:30].replace('\n', '')} ...\t[{len(chunk)}글자]")
    else:
        print(f"청크 {i+1}: {chunk[:30].replace('\n', '')} ...\t\t[{len(chunk)}글자]")



def embed_query(query):
    inputs = tokenizer(query, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].squeeze().numpy()


query = "고려병원의 장점은?"
query_vec = embed_query(query)


D, I = index.search(np.array([query_vec]), k=3)
print("가장 유사한 청크 인덱스:", I[0])

for idx in I[0]:
    print(f"청크 {idx+1} 미리보기:", chunks[idx][:100].replace('\n', ' '))









