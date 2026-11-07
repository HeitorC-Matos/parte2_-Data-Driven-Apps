# Chatbot simples com FastAPI e Fake LLM

## Objetivo

Criar uma API que recebe uma pergunta e devolve uma resposta simulada com o LangChain. As respostas são cadastradas no código, portanto o programa não gera textos novos como um modelo real.

## Arquivos

- `main.py`: aplicação FastAPI e respostas do chatbot.
- `requirements.txt`: bibliotecas necessárias.
- `arquitetura.png`: imagem do diagrama da aplicação.

## Preparação no VS Code (Windows)

1. Extraia o ZIP em uma pasta própria e abra essa pasta pelo menu **Arquivo > Abrir Pasta** do VS Code.
2. Abra **Terminal > Novo Terminal**.
3. Digite `dir` para verificar se `main.py` e `requirements.txt` estão nessa mesma pasta.
4. Crie o ambiente virtual:

   ```powershell
   py -m venv .venv
   ```

5. Instale as bibliotecas:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

6. Inicie a API na porta 8000:

   ```powershell
   .\.venv\Scripts\python.exe -m uvicorn main:app --reload
   ```

7. Acesse no navegador: http://127.0.0.1:8000/docs

Se outra aplicação já estiver usando a porta 8000, encerre-a com `Ctrl + C`, no terminal correspondente, ou use a porta 8001:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --port 8001
```

Nesse caso, acesse http://127.0.0.1:8001/docs.

## Testando

1. Abra `POST /conversar`.
2. Clique em **Try it out**.
3. Envie o exemplo:

   ```json
   {
     "mensagem": "O que é FastAPI?"
   }
   ```

4. Clique em **Execute**.

A resposta esperada é:

```json
{
  "resposta": "FastAPI é uma ferramenta do Python usada para criar APIs."
}
```

Outras perguntas aceitas:

- `Oi`
- `Olá`
- `O que é LangChain?`
- `O que é Fake LLM?`
- `Como você está?`

Para perguntas não cadastradas, a API responde: `Ainda não sei responder essa pergunta.`

## Funcionamento

O FastAPI recebe a mensagem em JSON e procura uma resposta no conjunto de perguntas cadastradas. Em seguida, o `FakeListLLM` do LangChain devolve a resposta simulada. Por último, o FastAPI entrega o resultado em JSON.

Usar um Fake LLM é útil para testar rapidamente se a aplicação recebe perguntas e devolve respostas. Ele não exige conexão com um serviço de inteligência artificial nem pagamento por chamadas, e permite saber antecipadamente qual resposta será devolvida.

## Observação

O Fake LLM não entende a pergunta nem cria uma resposta por conta própria. Ele serve para simular essa etapa durante o desenvolvimento e os testes.