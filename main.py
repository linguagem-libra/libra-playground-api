from fastapi import FastAPI, Request
import httpx

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Olá Mundo"}

@app.post("/executar")
async def encaminhar_requisicao(request: Request):
    url = "http://lucasof.com:5102/executar"
    body = await request.json()

    async with httpx.AsyncClient() as client:
        resposta = await client.post(url, json=body)

    return resposta.json()