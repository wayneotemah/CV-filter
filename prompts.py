import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

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
  
  





