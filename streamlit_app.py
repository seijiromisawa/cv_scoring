import streamlit as st
from gpt import SYSTEM_PROMPT, request_gpt
from parse_hh import get_candidate_info, get_job_description


st.title("CV Scoring App")
job_description_url = st.text_area("Enter the job description url")
cv_url = st.text_area("Enter the CV url")

if st.button("Score CV"):
    with st.spinner("Scoring CV..."):
        job_description = get_job_description(job_description_url)
        cv = get_candidate_info(cv_url)

        st.write("Job description:")
        st.write(job_description)
        st.write("CV:")
        st.write(cv)

        user_prompt = f"# ВАКАНСИЯ\n{job_description}\n\n# РЕЗЮМЕ\n{cv}"
        response = request_gpt(SYSTEM_PROMPT, user_prompt)
    
    st.write(response)