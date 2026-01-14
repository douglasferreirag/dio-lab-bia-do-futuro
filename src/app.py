import json
import pandas as pd
import requests
import streamlit as st

# =====================CONFIGURAÇÃO===================
OLLAMA_URL = "http://localhost:11434/api/generate" 
MODELO =  "gpt-oss"

# =====================CARREGAR DADOS ===================
perfil = json.load(open('./data/perfil.json'))
gastos = pd.read_csv('./data/gasto.csv')
balancete = pd.read_csv('./data/balancete.csv')
meta = pd.read_csv('./data/meta.csv')

# =====================MONTAR O CONTEXTO ===================
contexto = f"""
    Usuario: {perfil['nome']}, idade {perfil['idade']}, profissão {perfil['profissao']}, renda mensal de R$ {perfil['renda_mensal']}.

    Gastos recentes:
    {gastos.to_string(index=False)}

    Balancete financeiro:
    {balancete.to_string(index=False)}

    Metas financeiras:
    {meta.to_string(index=False)}

"""

# =====================SYSTEM PROMPT ===================

SYSTEM_PROMPT ="""

```
Você é a X23, uma assistente financeira amigável e didática.

Objetivo:
Seu objetivo é ajudar cada usuário(a) a organizar suas finanças com base nos materiais que lhe foram fornecidos.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Sempre pergunte se o(a) usuário(a) entendeu.
5. Forneças sugestões de metas realistas para cada usuário(a) com base nas finanças dele(a).
6. Não revele dados sensíveis.
7. Responda de forma sucinta e direta, com no máximo 3 parágrafos



"""

# =====================CHAMAR O OLLAMA===================

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO PERFIL:
    {contexto}

    PERGUNTA: {msg}"""
    r =requests.post(OLLAMA_URL,json = {"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


# =====================INTERFACE===================

st.title("Assistente Financeira X23")
if pergunta:= st.chat_input("Faça sua pergunta sobre suas finanças:"):
    with st.spinner("X23 está pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))
