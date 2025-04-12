import streamlit as st
from model import generate_comment

st.set_page_config(page_title="Code Commenter", layout="centered")
st.title("🧠 Automatic Code Commenting System")
st.markdown("Paste your Python code snippet below. We'll generate a summary comment explaining what it does!")

code_input = st.text_area("🔹 Your Code", height=250, placeholder="e.g. x = input('Type a number: ') ...")

if st.button("📝 Generate Comment"):
    if code_input.strip():
        with st.spinner("Analyzing code..."):
            comment = generate_comment(code_input)
        st.success("✅ Generated Comment:")
        st.code(comment, language="markdown")
    else:
        st.warning("Please paste a code snippet first.")
