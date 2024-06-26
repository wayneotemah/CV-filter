import streamlit as st
import pandas as pd
from pdf_reader import process_pdf_from_url
from prompts import get_score

# Streamlit App
st.title("Resume Scoring App")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    if 'resume' not in df.columns:
        st.error("The Excel file does not contain a 'resume' column.")
    else:
        scores = []
        summaries = []

        for resume_url in df['resume']:
            resume_text = process_pdf_from_url(resume_url)
            result = get_score(resume_text)
            
            if result:
                scores.append(result.score)
                summaries.append(result.summary)
            else:
                scores.append(None)
                summaries.append(None)

        df['score'] = scores
        df['summary'] = summaries

        st.download_button(
            label="Download Results as CSV",
            data=df.to_csv(index=False),
            file_name="resume_scores.csv",
            mime="text/csv",
        )

        st.write(df)
