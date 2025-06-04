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

@app.get("/testar-conexao")
async def testar():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get("http://lucasof.com:5102")
            return {"status": r.status_code, "ok": r.text[:100]}
    except Exception as e:
        return {"erro": str(e)}
