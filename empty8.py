import streamlit as st



import subprocess
import re
from transformers import MarianMTModel, MarianTokenizer
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

st.set_page_config(page_title="챗봇", page_icon=":robot_face:")
st.title(":red[NHIS]&nbsp;:blue[라마]&nbsp;_챗봇_  &nbsp;&nbsp;&nbsp; :robot_face:")

def translate_ko_en(text):

    trans_path = "./trans/ko-en"
    tokenizer = MarianTokenizer.from_pretrained(trans_path)
    model = MarianMTModel.from_pretrained(trans_path)

    tokens = tokenizer(text, return_tensors="pt", padding=True)
    generated_ids = model.generate(**tokens)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)



def translate_en_ko(text):

    model_path = "./trans/facebook_m2m100"
    tokenizer = M2M100Tokenizer.from_pretrained(model_path)
    model = M2M100ForConditionalGeneration.from_pretrained(model_path)
    
    tokenizer.src_lang = "en"
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id("ko"))
    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]



def run_llama8(question_en: str) -> str:
    prompt = f"<s>[INST] {question_en} Please answer in Korean language. Your response must be at least 150 characters and no more than 500 characters. Do not go below or beyond these limits. [/INST]"
    print(prompt)
    result = subprocess.run(
        [LLAMA_RUN_PATH, MODEL_PATH, "-p", prompt, "--temp", "0.7", "--top-k", "40"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return result.stdout.strip()






from collections import deque
import time
ansi_escape = re.compile(r'\x1B\[[0-9;]*[mK]')


def run_llama(question_en: str):
    prompt = f"<s>[INST] {question_en} Answer in Korean language. Answer between 100 and 200 characters. [/INST]"
    print(prompt)
    process = subprocess.Popen(
        [LLAMA_RUN_PATH, MODEL_PATH, "-p", prompt, "--temp", "0.7", "--top-k", "40"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=1,
        universal_newlines=True
    )

    message_area = st.chat_message("assistant").empty()  # 여기서 선언
    answer = ""

    while True:
        ch_raw = process.stdout.read(1)
        if not ch_raw:
            if process.poll() is not None:
                break
            continue

        ch = ch_raw
        ch = ansi_escape.sub("", ch)

        answer += ch

        clean_answer = (
            answer.replace("[INST]", "")
                  .replace("[/INST]", "")
                  .replace("<s>", "")
                  .replace("</s>", "")
                  .replace("[K", "")
                  .replace("Loading model", "")
                  .replace("<|im_end|>", "")
                  .replace("<|im_start|>", "")
                  .replace("--instruct", "")
                  .replace("--top-p", "")
                  .replace("-p", "")
                  .strip()
        )

        message_area.markdown(clean_answer)

    return answer.strip()









LLAMA_RUN_PATH = "D:\\model\\llama.cpp\\build\\bin\\Release\\llama-run.exe"
MODEL_PATH = "D:\\model\\llama-3-Korean-Bllossom-8B-Q4_K_M.gguf"





if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message[0]).write(chat_message[1])

question = st.chat_input("질문을 입력하세요.")
if question:
    st.chat_message("user").write(question)




    question_en = translate_ko_en(question)
    print(question_en)
    
    raw_answer = run_llama(question_en)
    print(raw_answer)
    print(7)

    
    answer = raw_answer   # translate_en_ko(raw_answer[:500])  # 너무 길면 번역 오류

    print(answer)



    # answer = "LLM 모델이 연결되지 않았습니다."









    
    st.chat_message("assistant").write(answer)

    st.session_state["messages"].append(["user", question])
    st.session_state["messages"].append(["assistant", answer])




















