# -*- coding: utf-8 -*-
"""Projeto Python 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U9Ulvtw3r4tjgaGgacf9ur5gMNwNLDBs
"""



"""**Projeto com objetivo de analisar faturamento das lojas, e realizar a demonstração de maneira gráfica.**"""

# Passo a passo da resolução do projeto
# Passo 1 - percorrer os arquivos da pasta "Vendas"
# Passo 2 - Importar as bases de dados de vendas
# Passo 3 - Tratar / compilar as bases de dados
# Passo 4 - Calcular o produto mais vendido (em quantidade)
# Passo 5 - Calcular o produto que mais faturou (em faturamento)
# Passo 6 - Calcular a loja/cidade que mais vendeu em faturamento (em faturamento) - criar um gráfico/dashboard

# Passo 1

import os
import pandas as pd
import plotly.express as px

lista_arquivos = os.listdir("/content/drive/MyDrive/Projeto Python 1/Vendas")
display(lista_arquivos)

tabela_total = pd.DataFrame()

# Passo 2
# Importar arquivos que contém "Vendas" no nome.

for arquivo in lista_arquivos:
  if "Vendas" in arquivo:
    tabela = pd.read_csv(f"/content/drive/MyDrive/Projeto Python 1/Vendas/{arquivo}")
    tabela_total = pd.concat([tabela_total, tabela], ignore_index= True)

#Passo 3
display(tabela_total)

# Passo 4

tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida", "Preco Unitario"]].sort_values("Quantidade Vendida", ascending=False)
display(tabela_produtos)

# Passo 5

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]

tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values("Faturamento", ascending=False)
display(tabela_faturamento)

# Passo 6

tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]].sort_values("Faturamento", ascending=False)
display(tabela_lojas)

# Gráfico

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico.show()