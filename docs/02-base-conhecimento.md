# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `balancete.csv` | CSV | Gerar visão mensal do total de gastos. |
| `perfil.json` | JSON | Identificar perfil com base em renda. |
| `metas.csv` | CSV | Registrar metas mensais |
| `gasto.csv` | CSV | Registrar despesas detalhadamente. |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

A tabela de gastos vai mostrar as despesas do usuário detalhadamente.
A tabela de balancete vai mostrar quanto o usuário gastou mensalmente.
O perfil demonstra o tipo do usuário e qual seu salário.
A tabela de metas mostra as metas mensais que o usuário não pode ultrapassar.

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
meta  = pd.read_csv('data.meta')

#JSONs

with open('data/perfil.json', 'r', encoding = 'utf-8') as p:

  produtos = json.load(p)

````

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

É sugerível simplificar o máximo possível. Podemos injetados também. Para ganhar flexibilidade, o ideal é que os dados sejam carregados dinamicamente.

``` text

#Dados do Perfil:

{
  
  "id": 1,
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  
}

#Dados do Gasto

data	descricao	categoria	valor	id_perfil
2025-10-01	Aluguel	moradia	1200.00	1
2025-10-02	Recarga para celular	comunicacao	250.00	1
2025-10-03	Supermercado	casa	450.00	1

#Dados da Meta

mês	ano	valor	id_perfil
1	2025	1000.00	1
2	2025	600.00	1
3	2025	500.00	1
4	2025	800.00	1
5	2025	300.00	1
6	2025	1000.00	1

#Dados do Balancete

mês	ano	total	id_perfil
1	2025	600.00	1
2	2025	500.00	1
3	2025	1000.00	1



```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Dados do Balancete

- mes: 1
- ano: 2025
- total: 600.00
- id_perfil: 1

Dados do Gasto

- data: 2025-10-01
- descricao: Aluguel	
- categoria: moradia
- valor: 1200.00
- id_perfil: 1


Dados do Perfil

- id: 1
- nome: João Silva
- profissao: Analista de Sistemas

Dados da Meta

-  mes: 1
- ano: 2025
- valor: 100
- id_perfil: 1


