import pandas as pd
import matplotlib.pyplot as plt

# r para indicar texto bruto
vendas_df = pd.read_csv(r"E:\basesDados\Contoso - Vendas - 2017.csv", sep=";") # com o separador
lojas_df = pd.read_csv(r"E:\basesDados\Contoso - Lojas.csv", sep=";")
produtos_df = pd.read_csv(r"E:\basesDados\Contoso - Cadastro Produtos.csv", sep=";")
clientes_df = pd.read_csv(r"E:\basesDados\Contoso - Clientes.csv", sep=";")

#alerta para o erro de encoding, quando há caracteres desconhecidos, acentuação ou especiais..etc
#irá dar erro na importação importante passar a codificação
#encoding="Latin1"  "encoding=ISO-8859-1"  encoding="utf-8"  encoding="cp1252"

#retirar informações inuteis da base dando um drop nas colunas inuteis
clientes_df = clientes_df.drop(["Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10"], axis=1) #eixo 1 colunas, eixo 0 linhas
#clientes_df = clientes_df.drop(["ID Cliente", "E-mail"]) #dropa as colunas
#produtos_df = produtos_df.drop(["ID Produto", "Nome do Produto"])
#lojas_df = lojas_df.drop(["ID Loja", "Nome da Loja"])

#após limpar a base do que não é útil, segue para o merge com os dataframes.
#realizar o merge com a coluna que faz referencia entre os dois dataframes, no exemplo abaixo está o ID Produto.
#merge dos dataframes vendas_df e produtos_df
#on refere-se a coluna, no caso o ID Produto

vendas_df = vendas_df.merge(produtos_df, on="ID Produto")
vendas_df = vendas_df.merge(lojas_df, on="ID Loja")
vendas_df = vendas_df.merge(clientes_df, on="ID Cliente")

#Rename para renomear colunas e linhas
vendas_df = vendas_df.rename(columns={"E-mail" : "E-mail do Cliente"}) #nome antigo e nome novo
#exibir o novo dataframe

#Qual cliente comprou mais vezes? Que veio na loja
#Metodo valueCount
#quantas vezes o cliente aparece no dataframe, inputa as colunas
freqClientes = vendas_df["E-mail do Cliente"].value_counts()
print(freqClientes)

#plota no grafico
#freqClientes.plot() # vai plotar todos
freqClientes[:5].plot(figsize=(15, 5)) #plota os primeiros 5 itens/clientes

plt.show()

#print(vendas_df)
#print(lojas_df)
#print(produtos_df)
#print(clientes_df)