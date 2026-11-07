import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI(title="Tradutor de inglês para francês")


class EntradaTexto(BaseModel):
    texto: str = Field(min_length=1)


prompt = ChatPromptTemplate.from_messages([
    ("system", "Traduza do inglês para o francês. Responda somente com a tradução."),
    ("human", "{texto}")
])

cadeia = None

if os.getenv("OPENAI_API_KEY"):
    modelo = ChatOpenAI(
        model="gpt-6-luna",
        reasoning_effort="none",
        timeout=30,
        max_retries=1
    )
    cadeia = prompt | modelo | StrOutputParser()


@app.post("/traduzir")
async def traduzir_texto(entrada: EntradaTexto):
    texto = entrada.texto.strip()

    if not texto:
        raise HTTPException(status_code=422, detail="Digite um texto em inglês.")

    if cadeia is None:
        raise HTTPException(status_code=503, detail="Configure a chave OPENAI_API_KEY no arquivo .env.")

    try:
        traducao = await cadeia.ainvoke({"texto": texto})
    except Exception as erro:
        raise HTTPException(
            status_code=502,
            detail="Não foi possível traduzir. Verifique a chave, os créditos e a conexão."
        ) from erro

    return {"texto_traduzido": traducao.strip()}
