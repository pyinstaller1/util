import streamlit as st
import subprocess
import collections
import json
import faiss
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel, MarianMTModel, MarianTokenizer

# -----------------------------
# LLaMA 경로
LLAMA_RUN_PATH = "D:\\model\\llama.cpp\\build\\bin\\Release\\llama-run.exe"
MODEL_PATH = "D:\\model\\llama-3-Korean-Bllossom-8B-Q4_K_M.gguf"

# -----------------------------
# FAISS와 청크 로드
index = faiss.read_index("vector_index.faiss")
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# -----------------------------
# 임베딩 모델 로드
tokenizer = AutoTokenizer.from_pretrained("./ko-sroberta-multitask")
model = AutoModel.from_pretrained("./ko-sroberta-multitask")
# model = AutoModel.from_pretrained("./ko-sroberta-multitask").cuda()
model.eval()

# -----------------------------
# 번역 모델 로드 (한글 → 영어)
TRANS_PATH = "./trans/ko-en"
tokenizer_trans = MarianTokenizer.from_pretrained(TRANS_PATH)
model_trans = MarianMTModel.from_pretrained(TRANS_PATH)
# model_trans = MarianMTModel.from_pretrained(TRANS_PATH).cuda()


def trans_en(text: str) -> str:
    """한글 문장을 영어로 번역"""
    tokens = tokenizer_trans(text, return_tensors="pt", padding=True)
    # tokens = tokenizer_trans(text, return_tensors="pt", padding=True).cuda()
    with torch.no_grad():
        generated_ids = model_trans.generate(**tokens)
    return tokenizer_trans.decode(
        generated_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True
    )

# -----------------------------
# Streamlit UI
st.set_page_config(page_title="NHIS 라마3 챗봇", page_icon=":robot_face:")
st.title(":red[NHIS] :blue[_라마3_] 챗봇 :robot_face:")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 이전 대화 출력
for role, msg in st.session_state["messages"]:
    st.chat_message(role).write(msg)

# 질문 입력
question = st.chat_input("질문을 입력하세요.")
if question:
    st.chat_message("user").write(question)

    # -----------------------------
    # 1. 질문 벡터화 + 유사 청크 검색
    inputs = tokenizer(question, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    query_vec = outputs.last_hidden_state[:, 0, :].squeeze().numpy()

    # D, I = index.search(np.array([query_vec]), k=3)
    # context = "\n".join([chunks[idx] for idx in I[0]])

    D, I = index.search(np.array([query_vec]), k=1)  # 가장 유사한 1개만 검색
    context = chunks[I[0][0]]


    # -----------------------------
    # 2. 질문 영어 번역
    question_en = trans_en(question)

    # -----------------------------
    # 3. LLaMA 프롬프트 구성 (context 포함)
    
    # prompt = f"<s>[INST] You are a helpful assistant. Please answer between 80 and 150 tokens in Korean.\n\n" \
    #         f"Question (translated): {question_en}\n\n" \
    #         f"Reference context:\n{context}\n\n" \
    #         f"Answer in Korean based only on the reference context. [/INST]"





    prompt = f"<s>[INST] Question (translated): {question_en}\n\n" \
             f"Answer based only on the reference context below. Do NOT include the reference context or any citation in your answer.\n\n" \
             f"{context}\n\n" \
             f"Do not include question in your answer.\n\n" \
             f"Tanslate your answer into Korean language and answer only it.\n\n" \
             f"[/INST]"




    # -----------------------------
    # 4. 참조 청크를 콘솔(cmd)에 출력
    print("\n=== 참조 청크 ===")
    for idx in I[0]:
        print(f"청크 {idx+1}: {chunks[idx][:].replace(chr(10), ' ')} ...")
    print("================\n")

    # -----------------------------
    # 5. LLaMA 실행
    process = subprocess.Popen(
        [LLAMA_RUN_PATH, MODEL_PATH, "-n", "256", "--temp", "0.7", "--top-p", "0.9", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        bufsize=1,
    )

    message_area = st.chat_message("assistant").empty()
    visible_text = ""
    deque = collections.deque()
    ignore_tokens = ["[INST]", "[/INST]", "<s>", "</s>", "Loading model", "[K", "[0m", "--top-p 0.9"]
    max_token_len = max(len(t) for t in ignore_tokens)

    while True:
        char = process.stdout.read(1)
        if char == "" and process.poll() is not None:
            break
        if not char:
            continue
        deque.append(char)
        token_buffer = "".join(deque)
        matched = False
        for token in ignore_tokens:
            if token_buffer.endswith(token):
                for _ in range(len(token)):
                    deque.pop()
                matched = True
                break
        if not matched and len(deque) > max_token_len:
            visible_text += deque.popleft()
            clean = visible_text.replace("보건보험", "건강보험").strip()
            message_area.write(clean)

    while deque:
        visible_text += deque.popleft()
        clean = visible_text.replace("보건보험", "건강보험").strip()
        message_area.write(clean)

    process.stdout.close()
    process.wait()

    # -----------------------------
    # 세션 상태에 저장
    st.session_state["messages"].append(("user", question))
    st.session_state["messages"].append(("assistant", clean))
