


from transformers import AutoTokenizer, AutoModel
import torch
import fitz  # PyMuPDF

def get_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text




def chunk_text(text, chunk_size=900, overlap=200):
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





def embed_chunk(chunk):
    inputs = tokenizer(chunk, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :]  # [CLS] 토큰
    return cls_embedding.squeeze().numpy()



text = ''
text += get_pdf(".\건강보험자료.pdf")
chunks = chunk_text(text, chunk_size=900, overlap=200)


for i, chunk in enumerate(chunks):
    print(f"청크 {i+1}: {chunk[:30].replace('\n', '')}\t[{len(chunk)}글자]")
print()




tokenizer = AutoTokenizer.from_pretrained("./ko-sroberta-multitask")
model = AutoModel.from_pretrained("./ko-sroberta-multitask")
model.eval()

chunk_embeddings = [embed_chunk(chunk) for chunk in chunks]


# 첫 번째 청크 토큰화
tokens = tokenizer.tokenize(chunks[0])
# print(tokens)

# 임베딩 벡터 앞 10차원
embedding_slice = chunk_embeddings[0][:10]

print("첫 번째 청크 토큰 10개:", tokens[:10])

# print(f"총 임베딩된 청크 수: {len(chunk_embeddings)}")
# print(f"임베딩 벡터 차원: {chunk_embeddings[0].shape}")
print(f"첫 번째 청크 임베딩 일부:\n{chunk_embeddings[0][:10]}")  # 앞 10개 값만 출력
print()






import faiss
import numpy as np

embedding_dim = chunk_embeddings[0].shape[0]
index = faiss.IndexFlatL2(embedding_dim)
index.add(np.array(chunk_embeddings))















inputs = tokenizer(chunks[0], return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)

token_vectors = outputs.last_hidden_state.squeeze(0)  # (토큰수, 768)
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

print('청크1의 토큰')
for i in range(8):
    print(f"토큰{i+1} {tokens[i]}\t", str(token_vectors[i][:5].numpy()).replace(']', ' ... ⇨ 768 차원 ]'))

print()










def embed_query(query):
    inputs = tokenizer(query, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].squeeze().numpy()

query = "고려병원의 장점은?"
query_vec = embed_query(query)

D, I = index.search(np.array([query_vec]), k=3)  # 상위 3개 청크 인덱스 검색
print("가장 유사한 청크 인덱스:", I)









