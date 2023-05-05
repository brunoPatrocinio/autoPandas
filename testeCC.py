import pandas as pd
import numpy
import openpyxl
import plotly.express as px

#importando a base de dados

tabela = pd.read_csv("C:\\Users\\bruno\\Downloads\\telecom_users.csv")
tabela = tabela.drop("Unnamed: 0", axis = 1) # axis 0 => linha, axis 1 => coluna

#tranformando uma coluna de texto para numero
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") #se der erros deleta aquela info, Coerce
#se tiver muitas linhas vazias, talvez seja preciso avaliar substituir por algum dado para preencher

#deletando as colunas vazias
tabela = tabela.dropna(how="all", axis=1) #como ele vai fazer, e se é linhas vazias ou colunas vazias all=>todos vazios
#linhas que tem pelo menos um valor vazio
tabela = tabela.dropna(how="any", axis=0) #como ele vai fazer, e se é linhas vazias ou colunas vazias any=> algum valor vazio

#jogar as informações que são vazias para não atrapalhar a análise.

#parte de análise como estão os cancelamentos da plataforma?
#análise inicial
#Quantas pessoas cancelaram e qunats não
#tabela["Churn"].value_counts()

print(tabela.info())

print(tabela["Churn"].value_counts())
#print(tabela["Churn"].value_counts(normalize=True)) #em percentual

print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #em percentual formatado, uma casa decimal

#parte de análise mais completa, com comparação. comparar cada coluna da tabela com a coluna de cancelamento.
#criar o gráfico
grafico = px.histogram(tabela, x="Casado") #seleciona o tipo do grafico passando a tabela e a coluna de exibição. o Y ele cria automatico

#exibir o grafico
grafico.show()

#exportar a analise
tabela.to_excel("C:\\Users\\bruno\\Downloads\\resultado.xlsx")

#print(tabela)