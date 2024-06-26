import streamlit as st
import pandas as pd
from pdf_reader import process_pdf_from_url
from prompts import get_score

# Streamlit App
st.title("Resume Scoring App")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Check if 'resume' column exists
    if 'resume' not in df.columns:
        st.error("The Excel file does not contain a 'resume' column.")
    else:
        # Process Resumes and Get Scores
        scores = []
        summaries = []

        for resume_url in df['resume']:
            resume_text = process_pdf_from_url(resume_url)
            result = get_score(resume_text)
            
            if result:
                # Assuming your get_score function returns a dictionary with 'score' and 'summary' keys
                scores.append(result.score)
                summaries.append(result.summary)
            else:
                scores.append(None)
                summaries.append(None)

        # Add Scores and Summaries to DataFrame
        df['score'] = scores
        df['summary'] = summaries

        # Download Button
        st.download_button(
            label="Download Results as CSV",
            data=df.to_csv(index=False),
            file_name="resume_scores.csv",
            mime="text/csv",
        )

        # Display Results
        st.write(df)
