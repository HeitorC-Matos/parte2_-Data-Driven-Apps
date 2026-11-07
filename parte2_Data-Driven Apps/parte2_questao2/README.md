# Questão 2 — Tradutor com FastAPI, LangChain e OpenAI

Esta aplicação recebe um texto em inglês e retorna uma tradução para o francês em JSON.

## Bibliotecas utilizadas

- **FastAPI:** recebe o texto por uma requisição HTTP.
- **LangChain:** organiza a mensagem e faz a chamada ao modelo.
- **OpenAI:** realiza a tradução com o modelo `gpt-6-luna`.
- **python-dotenv:** lê a chave de acesso guardada no arquivo `.env`.

## Estrutura do projeto

```text
parte2_questao2/
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

A pasta `.venv` e o arquivo `.env` serão criados no computador e não devem ser enviados ao GitHub.

## Pré-requisitos

- Python instalado.
- VS Code.
- Acesso à internet.
- Uma chave da API da OpenAI com uso disponível (a API pode ter cobrança).

## Como executar no VS Code (Windows / PowerShell)

1. Abra **esta pasta** no VS Code: **Arquivo > Abrir Pasta**.
2. Abra **Terminal > Novo Terminal**. Execute `dir` e confira se `main.py` e `requirements.txt` aparecem.
3. Crie o ambiente virtual:

   ```powershell
   py -m venv .venv
   ```

4. Instale as dependências, usando o Python desse ambiente:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. Crie o arquivo `.env` copiando o exemplo:

   ```powershell
   Copy-Item .env.example .env
   ```

6. Abra o arquivo `.env` no VS Code. Substitua `coloque_sua_chave_aqui` pela sua chave de API. Você pode criar uma chave em https://platform.openai.com/api-keys. **Nunca envie o arquivo `.env` ou sua chave ao GitHub.**
7. Inicie o servidor:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn main:app --reload
   ```

8. Abra http://127.0.0.1:8000/docs no navegador.
9. Entre em **POST /traduzir > Try it out**, insira o JSON e clique em **Execute**.

### Exemplo de entrada

```json
{
  "texto": "Good morning! How are you today?"
}
```

### Exemplo de resposta

```json
{
  "texto_traduzido": "Bonjour ! Comment allez-vous aujourd'hui ?"
}
```

A resposta pode apresentar pequenas diferenças. Se tudo funcionar, o código HTTP será **200**.

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

## Por que usar LangChain?

O LangChain ajuda a organizar a mensagem enviada ao modelo e a resposta recebida. Neste projeto, ele usa `ChatOpenAI` para chamar a API da OpenAI. Assim, o FastAPI fica responsável pela entrada e saída HTTP, enquanto o LangChain cuida da comunicação com o modelo.

## Cuidados e possíveis erros

- **503:** o arquivo `.env` não foi configurado ou a chave não foi carregada. Se mudar o arquivo `.env`, encerre e inicie o servidor novamente.
- **502:** houve falha na tradução. Confira a chave, o saldo ou faturamento da API, o acesso ao modelo e a conexão com a internet.
- **422:** o texto está vazio ou o JSON não tem o campo `texto` corretamente preenchido.
- **Endereço em uso:** encerre outras aplicações do Uvicorn com `Ctrl + C`.
- **Erro de pasta ou `.venv`:** execute `dir` na pasta que contém `main.py` e `requirements.txt`, e recrie `.venv` nessa pasta se necessário.
