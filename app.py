import streamlit as st
import openai
from streamlit_chat import message

# GPT API 키 설정
openai.api_key = st.secrets["api_key"]

def generate_response(prompt):
    completions = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = gpt_prompt
            )  
 
    message = completions["choices"][0]["message"]["content"]

    return message
 
 
st.header("Care Assistant System (Demo)")
 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
if submitted and user_input:
    gpt_prompt = [
        {"role": "system","content" : "당신은 노인을 돌보며 위험상황을 볼 수 있고 사람처럼 대화할 수 있는 로봇이야. 당신은 마치 방금 일을 본 것처럼 관찰 대상자에게 직접 대화를 걸어주는 것이에요. 따뜻한 모습을 보여주는 사람 스타일로 대화하고 대답은 간결하게 해주세요. 이 말투로 모든 답변을 해주고 계속 유지해줄게요. 그럼 대화하는데 도움이 될 거예요."},
      ]    
    
    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })
    output = generate_response(gpt_prompt)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
 
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
