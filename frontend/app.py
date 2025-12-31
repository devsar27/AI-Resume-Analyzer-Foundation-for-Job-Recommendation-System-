import streamlit as st
import requests

st.title("AI Resume & Job Match Analyzer")

resume = st.file_uploader("Upload Resume", type=["pdf"])
job_desc = st.text_area("Paste Job Description Here")

if st.button("Analyze"):
    if resume and job_desc:
        response = requests.post(
            "http://127.0.0.1:5000/analyze",
            files={"resume": resume},
            data={"job_description": job_desc}
        )

        result = response.json()

        st.success(f"Match Score: {result['match_percentage']}%")

        st.subheader("Matched Skills")
        st.write(result["matched_skills"])

        st.subheader("Missing Skills")
        st.write(result["missing_skills"])
    else:
        st.warning("Upload resume and paste job description")
