# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `balancete.csv` | CSV | Gerar visão mensal do total de gastos. |
| `perfil.json` | JSON | Identificar perfil com base em renda e metas. Personalizar recomendações com base nelas. |
| `gastos.csv` | CSV | Registrar despesas detalhadamente. |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

A tabela  gastos vai mostrar as despesas do usuário detalhadamente.
A tabela balancete vai mostrar quanto o usuário gastou mensalmente.
O perfil demonstra o tipo do usuário, qual seu salário e as metas de gastos no mês.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

````python

Existe duas possibilidades: injetar diretamente no prompt (CTRL + C, CTRL + V ) ou carregar os arquivos via código, como no exemplo abaixo.

#CSVs

import pandas as pd
import json

gastos = pd.read_csv('data.gastos')
balancete  = pd.read_csv('data.balancete')

#JSONs

with open('data/perfil.json', 'r', encoding = 'utf-8') as p:

  produtos = json.load(p)

````

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Sim
Sim

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

``` text
Dados do Cliente:
- Nome: João Silva
- Meta: R$ 2.500
- Gasto no mês 12: R$ 5.000


...
```
