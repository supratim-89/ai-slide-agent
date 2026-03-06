from fastapi import FastAPI
from app.graph import workflow

app = FastAPI()

@app.post("/generate")
async def generate_slide(prompt:str):

    result = workflow.invoke({"prompt":prompt})

    return {
        "message":"Presentation generated",
        "file":"artifacts/generated_deck.pptx"
    }