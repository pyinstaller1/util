from langchain_openai import ChatOpenAI
import os
import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from transformers import MarianMTModel, MarianTokenizer
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def translate_ko_ja(text):
    model_path = "./facebook_m2m100"
    tokenizer = M2M100Tokenizer.from_pretrained(model_path)
    model = M2M100ForConditionalGeneration.from_pretrained(model_path)
    
    tokenizer.src_lang = "ko"
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id("ja"))
    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]

def translate_ja_ko(text):
    model_path = "./facebook_m2m100"
    tokenizer = M2M100Tokenizer.from_pretrained(model_path)
    model = M2M100ForConditionalGeneration.from_pretrained(model_path)
    
    tokenizer.src_lang = "ja"
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id("ko"))
    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]


def translate_ko_en(text):
    ko_en_path = "./ko-en"
    tokenizer = MarianTokenizer.from_pretrained(ko_en_path)
    model = MarianMTModel.from_pretrained(ko_en_path)
    
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    generated_ids = model.generate(**tokens)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)



def translate_en_ko(text):
    model_path = "./facebook_m2m100"
    tokenizer = M2M100Tokenizer.from_pretrained(model_path)
    model = M2M100ForConditionalGeneration.from_pretrained(model_path)
    
    tokenizer.src_lang = "en"
    encoded = tokenizer(text, return_tensors="pt")
    generated = model.generate(**encoded, forced_bos_token_id=tokenizer.get_lang_id("ko"))
    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]





def translate_en_ja(text):
    en_ja_model_path = "./en-ja"
    tokenizer = MarianTokenizer.from_pretrained(en_ja_model_path)
    model = MarianMTModel.from_pretrained(en_ja_model_path)
    
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    output = model.generate(**inputs)
    return tokenizer.decode(output[0], skip_special_tokens=True)


def translate_ja_en(text):

    ja_en_model_path = "./ja-en"
    tokenizer = MarianTokenizer.from_pretrained(ja_en_model_path)
    model = MarianMTModel.from_pretrained(ja_en_model_path)
    
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    output = model.generate(**inputs)
    return tokenizer.decode(output[0], skip_special_tokens=True)





# 사이드바 설정
with st.sidebar:
    st.header("⚙️ 번역 모드 선택")
    
    # 사용자가 선택할 수 있는 번역 옵션
    translation_mode = st.selectbox(
        "원하시는 번역 방향을 선택하세요:",
        (
            "한국어-일본어", 
            "일본어-한국어", 
            "한국어-영어", 
            "영어-한국어",
            "영어-일본어",
            "일본어-영어"
        ),
        index=0 # 기본값 설정
    )

# 선택된 모드에 따라 제목과 함수 매핑
mode_config = {
    "한국어-일본어": {"title": ":red[_NHIS_]&nbsp;한국어-日本語&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;🌸", "function": translate_ko_ja},
    "일본어-한국어": {"title": ":red[_NHIS_]&nbsp;日本語-한국어&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;🌸", "function": translate_ja_ko},
    "한국어-영어": {"title": ":red[_NHIS_]&nbsp;한영&nbsp;⭐&nbsp;&nbsp;:blue[번역]&nbsp;:robot_face:", "function": translate_ko_en},
    "영어-한국어": {"title": ":red[_NHIS_]&nbsp;영한&nbsp;⭐&nbsp;&nbsp;:blue[번역]&nbsp;:robot_face:", "function": translate_en_ko},
    "영어-일본어": {"title": ":red[_NHIS_]&nbsp;한국어-日本語&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;🌸", "function": translate_en_ja},
    "일본어-영어": {"title": ":red[_NHIS_]&nbsp;日本語-한국어&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;🌸", "function": translate_ja_en},    
}

# 선택된 모드에 따라 제목 설정
st.title(mode_config[translation_mode]["title"])




# st.title(":red[_NHIS_]&nbsp;日本語-영어&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;:robot_face:")
# st.title(":red[_NHIS_]&nbsp;영어-日本語&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;:robot_face:")


# st.title(":red[_NHIS_]&nbsp;日本語-한국어&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;🌸")
# st.title(":red[_NHIS_]&nbsp;한국어-日本語&nbsp;🔴&nbsp;&nbsp;:blue[번역]&nbsp;🌸")

# st.title(":red[_NHIS_]&nbsp;영한&nbsp;⭐&nbsp;&nbsp;:blue[번역]&nbsp;:robot_face:")
# st.title(":red[_NHIS_]&nbsp;한영&nbsp;⭐&nbsp;&nbsp;:blue[번역]&nbsp;:robot_face:")



if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message[0]).write(chat_message[1])

question = st.chat_input("질문을 입력하세요.")
if question:
    st.chat_message("user").write(question)

    # answer = translate_ko_ja(question)
    # answer = translate_en_ko(question)
    # これはペンです。


    # 선택된 모드의 함수 호출
    translator_func = mode_config[translation_mode]["function"]
    
    with st.spinner(f"'{translation_mode}' 번역 중..."):
        answer = translator_func(question)
    








    
    st.chat_message("assistant").write(answer)
    

    st.session_state["messages"].append(["user", question])
    st.session_state["messages"].append(["assistant", answer])

