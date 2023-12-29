import io
import os
from click import File
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Form, UploadFile
from Question_model import question
import uvicorn
import google.generativeai as ai
from PIL import Image



app = FastAPI()
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)

load_dotenv()
apiKey = os.getenv("key")
ai.configure(api_key=apiKey)
model = ai.GenerativeModel('gemini-pro')
model_image = ai.GenerativeModel('gemini-pro-vision')

@app.get("/")
async def homepage():
  return {"Status":"Ready"}


@app.post("/img")
async def askimg(Ques:str= Form(...),file: UploadFile = File(None)):
    result:any
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        result = model_image.generate_content([Ques, image])
    except:
        result = model.generate_content(Ques)
    return result.text
