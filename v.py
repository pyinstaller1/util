



import fitz  # PyMuPDF

def get_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text




def chunk_text(text, chunk_size=1000, overlap=200):
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





text = ''
# text += get_pdf(".\건강보험자료.pdf")
# chunks = chunk_text(text, chunk_size=1000, overlap=200)


'''
print(f"총 청크 개수: {len(chunks)}")
print(chunks[0])   # 첫 번째 청크 내용 출력
print(len(chunks[0]))
'''























from transformers import AutoTokenizer, AutoModel
import torch

# 모델 로드 (오프라인 경로라면 해당 디렉토리로 바꾸세요)
model_path = "./ko-sroberta-multitask"  # 로컬 디렉토리 사용
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)

# 입력 문장
text = "나는 학생이다"

# 토크나이즈 및 텐서 변환
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# 모든 토큰의 임베딩 벡터 추출: shape = (1, 토큰수, 768)
token_embeddings = outputs.last_hidden_state[0]  # shape: (토큰수, 768)

# 토큰 확인
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# 결과 출력
for i, (token, vec) in enumerate(zip(tokens, token_embeddings)):
    print(f"\n🟢 Token {i}: '{token}'")
    print(f"🔢 Vector (768-dim):\n{vec.tolist()[:10]} ...")  # 처음 10개만 보기 좋게





















