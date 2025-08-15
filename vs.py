import streamlit as st
import subprocess
import re
from transformers import MarianMTModel, MarianTokenizer, AutoTokenizer, AutoModel
import torch

import faiss, json
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)









# -----------------------------
# RAG: FAISS + JSON 로컬
index = faiss.read_index("vector_index.faiss")
with open("chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

tokenizer_embed = AutoTokenizer.from_pretrained("./ko-sroberta-multitask")
model_embed = AutoModel.from_pretrained("./ko-sroberta-multitask")
model_embed.eval()

def embed_query(query):
    inputs = tokenizer_embed(query, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model_embed(**inputs)
    return outputs.last_hidden_state[:,0,:].squeeze().numpy()

def retrieve_context(query, top_k=1):
    print(query)
    query_vec = embed_query(query)
    D, I = index.search(np.array([query_vec]), k=top_k)
    print(777)

    for rank, idx in enumerate(I[0]):
        print(f"청크{idx+1}: { chunks[idx]}")


    context_texts = [chunks[idx] for idx in I[0]]
    return "\n".join(context_texts)





trans_path = "./trans/ko-en"
tokenizer = MarianTokenizer.from_pretrained(trans_path)
model = MarianMTModel.from_pretrained(trans_path)

def translate(text):
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    generated_ids = model.generate(**tokens)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)






def split_sentences_korean(text):
    sentences = re.split(r'(?<=[.!?])\s*', text)    # 마침표, 물음표, 느낌표 뒤에서만 문장 분리

    return [s.strip() for s in sentences if s.strip()]






























LLAMA_RUN_PATH = "D:\\model\\llama.cpp\\build\\bin\\Release\\llama-run.exe"
MODEL_PATH = "D:\\model\\llama-3-Korean-Bllossom-8B-Q4_K_M.gguf"

st.set_page_config(page_title="챗봇", page_icon=":robot_face:")
st.title(":red[NHIS] :blue[_라마3_] 챗봇 :robot_face:")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for role, msg in st.session_state["messages"]:
    st.chat_message(role).write(msg)

question = st.chat_input("질문을 입력하세요.")
if question:
    st.chat_message("user").write(question)

    translated = translate(question)
    context_text = retrieve_context(translated)   # RAG 청크




    # question_trans = f"Please answer between 80 and 150 tokens in Korean. {translated}\n\n관련 내용:\n{context_text}"
    # question_trans = "Please answer between 80 and 150 tokens in Korean. " + translated


    context_sentences = split_sentences_korean(context_text)

    translated_context = "\n".join(translate(sent) for sent in context_sentences)

    question_trans = (
        f"Please answer between 80 and 150 tokens in Korean. {translated}\n\n"
        f"관련 내용:\n{translated_context}"
        )



    # print("번역문:", question_trans)  # 디버그 출력

    prompt = f"<s>[INST] {question_trans} [/INST]"

    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')

    process = subprocess.Popen(
        [LLAMA_RUN_PATH, MODEL_PATH, "-n", "256", "--temp", "0.7", "--top-p", "0.9", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding='utf-8',
        bufsize=1,
    )

    message_area = st.chat_message("assistant").empty()
    # message_area.write("답변 생성중...")

    answer = ""






    import collections

    ignore_tokens = ["[INST]", "[/INST]", "<INST>", "</INST>", "<|INST>", "<|INST|>", "</INST|>", "Loading model8", "<s>", "</s>", "[K", "[0m", "--top-p 0.9", "���� ����:"]
    token_buffer = ""
    visible_text = ""
    deque = collections.deque()
    max_token_len = max(len(t) for t in ignore_tokens)


    answer_session = ""

    while True:
        char = process.stdout.read(1)
        if char == "" and process.poll() is not None:
            break
        if not char:
            continue

        deque.append(char)
        token_buffer = ''.join(deque)

        # 금지 토큰이 발견되면, 해당 길이만큼 삭제
        matched = False
        for token in ignore_tokens:
            if token_buffer.endswith(token):
                # 금지어가 끝에 매치되면 그만큼 제거
                for _ in range(len(token)):
                    deque.pop()
                matched = True
                break

        # 토큰이 없고 deque 길이가 충분하면 앞글자 출력
        if not matched and len(deque) > max_token_len:
            visible_text += deque.popleft()
            clean = visible_text.replace("보건보험", "건강보험").replace("Loading model", "").strip()
            message_area.write(clean)



    
    # 남은 글자 출력
    while deque:
        visible_text += deque.popleft()
        clean = visible_text.replace("보건보험", "건강보험").replace("Loading model", "").strip()
        message_area.write(clean)
    











    process.stdout.close()
    process.wait()

    st.session_state["messages"].append(("user", question))
    st.session_state["messages"].append(("assistant", clean))





















    
