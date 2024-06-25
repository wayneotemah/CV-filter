import logging
import os
from dotenv import load_dotenv

from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from .messages import *
from .parsers import Response
load_dotenv()

model = chat_Stuctured = ChatGroq(
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
).with_structured_output(Response)



def get_score(text):
  try:
    prompt = ChatPromptTemplate.from_messages([("system", SysMessage), ("human", text)])
    chain = prompt | chat_Stuctured
    results = chain.invoke({"text": ""})
    return results

  except Exception as e:
    print(e)
    return []