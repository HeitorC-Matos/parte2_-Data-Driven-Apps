# Questão 3 — Tradução com FastAPI, LangChain e Hugging Face

## Objetivo

Receber um texto em inglês por uma requisição HTTP e devolver a tradução para o alemão em JSON. O modelo utilizado é `Helsinki-NLP/opus-mt-en-de`.

## Ferramentas utilizadas

- **FastAPI:** recebe a requisição e envia a resposta.
- **Transformers:** carrega o modelo de tradução da Hugging Face.
- **LangChain:** usa `HuggingFacePipeline` para executar a tradução com `invoke`.
- **Pydantic:** verifica se o campo `texto` foi informado.

O modelo roda no próprio computador. Não é necessária uma chave da OpenAI nem da Hugging Face para baixar este modelo público.

## Estrutura do projeto

```text
parte2_questao3_tradutor_huggingface/
├── main.py
├── requirements.txt
├── README.md
```

## Como executar no VS Code (Windows)

1. Abra a pasta que contém `main.py` e `requirements.txt` no VS Code.
2. Abra **Terminal > Novo Terminal** e execute `dir` para verificar os arquivos.
3. Crie um ambiente virtual na pasta do projeto:

   ```powershell
   py -m venv .venv
   ```

4. Instale as bibliotecas usando o Python **desta questão**:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. Inicie a aplicação com o mesmo Python:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn main:app --reload
   ```

6. Abra `http://127.0.0.1:8000/docs`.
7. Acesse **POST /traduzir > Try it out**, insira o JSON abaixo e clique em **Execute**:

   ```json
   {
     "texto": "Good morning! I am learning Python."
   }
   ```

8. Confira se aparece o código **200** e o campo `texto_traduzido` em alemão.

   Exemplo de resposta possível:

   ```json
   {
     "texto_traduzido": "Guten Morgen! Ich lerne Python."
   }
   ```

O texto exato pode variar conforme o modelo.

## Outro teste

```json
{
  "texto": "The school is near my house. I study programming every day."
}
```

## Funcionamento

A API recebe o texto, separa entradas maiores em trechos de até 300 tokens (pequenas partes do texto), passa cada trecho ao LangChain e reúne as traduções. Separar os trechos pode prejudicar o contexto de textos longos, por isso a solução é um protótipo simples.

**Por que usar LangChain?** Ele oferece uma forma padronizada de chamar modelos. Neste projeto, `HuggingFacePipeline` liga o LangChain ao tradutor da Hugging Face.

## Atenção

- Na primeira execução, o modelo será baixado da Hugging Face. É necessária conexão à internet.
- O download e a primeira inicialização podem demorar. A tradução posterior ocorre localmente.
- O pacote `transformers` foi limitado à versão **4**, pois o pipeline `translation` não é suportado na versão **5**.
- Se `py -m venv .venv` utilizar uma versão do Python incompatível com alguma biblioteca, use Python 3.14 e recrie o ambiente virtual.
- Para encerrar o servidor, pressione `Ctrl + C` no terminal.

## Referências

- Modelo: https://huggingface.co/Helsinki-NLP/opus-mt-en-de
- Integração LangChain: https://reference.langchain.com/python/langchain-huggingface/llms/huggingface_pipeline/HuggingFacePipeline
