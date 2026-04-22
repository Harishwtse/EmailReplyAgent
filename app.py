import streamlit as st
from agents import run_agents

st.set_page_config(page_title="ReplyGeniAI Email Agent")
st.title("ReplyGeniAI Email Agent")
email = st.text_area("Hi, I purchased a laptop , curently it is not working.")

if st.button("Generate Reply"):
    if email.strip() == "":
        st.warning("Please Enter the vallied email text")
    else:
        result = run_agents(email)

        st.subheader("Detected Intent")
        st.success(result["intent"])

        st.subheader("Select Tone")
        st.info(result["tone"])

        st.subheader("Generated Reply")
        st.write(result["reply"])
