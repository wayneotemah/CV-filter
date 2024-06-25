import logging
import os
from dotenv import load_dotenv

from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from pdf_reader import process_pdf_from_url
from parsers import Response
from messages import SystemMessage
load_dotenv()


model = chat_Stuctured = ChatGroq(
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
).with_structured_output(Response)



def get_score(text):
  try:
    prompt = ChatPromptTemplate.from_messages([("system", SystemMessage), ("human", text)])
    chain = prompt | model
    results = chain.invoke({"text": ""})
    return results

  except Exception as e:
    print(e)
    return None
  
  
pdf_url = "http://demo.academy.adanianlabs.io/storage/uploads/dlt/resumes/c055a9c9-80df-4141-900c-25b16cd8e5c6.pdf"
resume_text = process_pdf_from_url(pdf_url)


results = get_score(resume_text)

print(results)


