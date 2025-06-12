import streamlit as st
import  google.generativeai as genai
import os

st.set_page_config(page_title="Chatbot",layout="centered",page_icon="Screenshot 2025-05-29 131424 - Copy.png",initial_sidebar_state='collapsed',menu_items={
    "About":"https://profile-59jw7xey2hvfc5gmtth4cu.streamlit.app/"
})
side=st.sidebar
with side:
    st.subheader("Place your Custom ApiKey:",divider=True)
    global apikey
    apikey=st.text_input("Enter Your API Key")
    st.link_button("Generate API Key",url="https://aistudio.google.com/apikey",type='tertiary')

apikey=os.environ["GOOGLE_API_KEY"]="AIzaSyDwy-SLCowgdmaY0axSjmtb0L8rtpTx4Nc"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-1.5-flash")

st.title("Chat With Gemini")
st.header("",divider=True)
a=st.chat_input()
st.logo("Screenshot_2025-05-29_131424-removebg-preview (1).png",size="large",link="https://profile-59jw7xey2hvfc5gmtth4cu.streamlit.app/")


if a:
    try:
        text=model.generate_content(a)
        st.write(f"**You:**  {a}")
        st.write(f"**ChatBot:**  {text.text}")
        pass
        
    except:
        st.warning("Error Generated ")



    
