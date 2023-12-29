import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import google.generativeai as ai

class question(BaseModel):
   Question:str

app = FastAPI()
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)

load_dotenv()
apiKey = os.getenv("key")
ai.configure(api_key=apiKey)
model = ai.GenerativeModel('gemini-pro')

@app.get("/")
async def homepage():
  return {"Status":"Ready"}

@app.post("/question")
async def ask(Ques:question):
    return model.generate_content(Ques.Question).text
  
