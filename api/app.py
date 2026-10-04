from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn 
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(title="LangChain Server",version="1.0",description="A Simple API Server")

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.environ["OPENAI_API_KEY"]
)
# llm = Ollama(
#     model="llama2" 
# )

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")

add_routes(app,prompt1|model,path="/essay")

prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words.")
add_routes(app,prompt2|model,path="/poem")

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)