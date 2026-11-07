from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from langchain_core.language_models.fake import FakeListLLM

app = FastAPI(title="Chatbot com Fake LLM")

respostas = {
    "oi": "Olá! Como posso ajudar?",
    "olá": "Olá! Como posso ajudar?",
    "o que é fastapi?": "FastAPI é uma ferramenta do Python usada para criar APIs.",
    "o que é langchain?": "LangChain ajuda a desenvolver aplicações que usam modelos de linguagem.",
    "o que é fake llm?": "Fake LLM é uma simulação usada para testar respostas sem um modelo real.",
    "como você está?": "Estou funcionando corretamente!"
}


class EntradaMensagem(BaseModel):
    mensagem: str = Field(min_length=1)


@app.post("/conversar")
def conversar(entrada: EntradaMensagem):
    pergunta = entrada.mensagem.strip().lower()

    if not pergunta:
        raise HTTPException(status_code=422, detail="Digite uma mensagem.")

    resposta = respostas.get(pergunta, "Ainda não sei responder essa pergunta.")
    modelo_falso = FakeListLLM(responses=[resposta])

    return {"resposta": modelo_falso.invoke(entrada.mensagem)}
