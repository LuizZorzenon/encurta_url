from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Bem vindo a API de encurtador de URL! -by Zorzenon_Dev"