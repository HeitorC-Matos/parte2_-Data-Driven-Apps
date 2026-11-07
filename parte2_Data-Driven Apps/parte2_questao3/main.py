from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

app = FastAPI(title="Tradutor de inglês para alemão")

tradutor_hf = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-de",
    max_length=512
)
tradutor = HuggingFacePipeline(pipeline=tradutor_hf)


class EntradaTexto(BaseModel):
    texto: str = Field(min_length=1)


@app.post("/traduzir")
def traduzir_texto(entrada: EntradaTexto):
    texto = entrada.texto.strip()

    if not texto:
        raise HTTPException(status_code=422, detail="Digite um texto em inglês.")

    tokens = tradutor_hf.tokenizer.encode(texto, add_special_tokens=False)
    traducoes = []

    for inicio in range(0, len(tokens), 300):
        parte = tradutor_hf.tokenizer.decode(
            tokens[inicio:inicio + 300], skip_special_tokens=True
        )
        traducoes.append(tradutor.invoke(parte))

    return {"texto_traduzido": " ".join(traducoes)}
