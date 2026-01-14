# Passo a passo da execução

1️⃣ Importação das bibliotecas

O Python carrega as bibliotecas necessárias:

json: para ler dados do perfil do usuário

pandas: para manipular arquivos CSV

requests: para fazer requisições HTTP ao Ollama

streamlit: para criar a interface web interativa

2️⃣ Configuração do modelo e da API

São definidos dois parâmetros principais:

OLLAMA_URL: endereço da API local do Ollama

MODELO: nome do modelo que será usado (gpt-oss)

Esses dados serão usados sempre que uma pergunta for enviada ao modelo.

3️⃣ Carregamento dos dados

O aplicativo lê os arquivos da pasta data:

perfil.json → informações pessoais do usuário

gasto.csv → gastos recentes

balancete.csv → resumo financeiro

meta.csv → metas financeiras

Esses dados ficam armazenados em variáveis (perfil, gastos, balancete, meta).

4️⃣ Montagem do contexto

Todos os dados carregados são organizados em uma única string (contexto), que inclui:

Dados do usuário (nome, idade, profissão, renda)

Tabela de gastos

Balancete financeiro

Metas financeiras

Esse contexto será enviado ao modelo para garantir que a resposta seja baseada apenas nesses dados.

5️⃣ Definição do System Prompt

O SYSTEM_PROMPT estabelece o comportamento da assistente X23:

Define o papel da IA (assistente financeira)

Impõe regras claras (não inventar dados, ser sucinta, perguntar se o usuário entendeu, etc.)

Limita o tamanho e o estilo das respostas

Esse texto funciona como “instruções fixas” para o modelo.

6️⃣ Função perguntar(msg)

Quando o usuário faz uma pergunta:

O código junta:

SYSTEM_PROMPT

contexto

A pergunta do usuário (msg)

Envia tudo em um POST para a API do Ollama

Recebe a resposta em JSON

Retorna apenas o texto da resposta (response)

7️⃣ Criação da interface com Streamlit

st.title() exibe o título da aplicação

st.chat_input() cria o campo de pergunta no estilo chat

Quando o usuário digita algo:

O texto é armazenado em pergunta

Um spinner aparece indicando processamento

A função perguntar(pergunta) é chamada

A resposta da X23 é exibida como mensagem do assistente

8️⃣ Resultado final

O usuário:

Digita uma pergunta sobre suas finanças

A X23 analisa os dados reais carregados

O modelo responde seguindo todas as regras do system prompt

A resposta aparece na interface do chat

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)

```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

# Código completo

Todo código está no app.py

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

#ollama
Garantir que o ollama está rodando

# Rodar a aplicação
streamlit run app.py
```
