import streamlit as st
import requests

st.title("AI Resume Analyzer")

uploaded = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded:
    response = requests.post(
        "http://localhost:5000/analyze",
        files={"resume": uploaded}
    )
    data = response.json()

    st.success(f"Resume Score: {data['score']}")
    st.write("Detected Skills:")
    st.write(data["skills"])
