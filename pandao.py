#arquivos csv e dataframes
#Temos um dataframe chamado vendas_df

#vendas_df['coluna_x'] -> uma lista com os valores da coluna_x (em formato dataframe, é um dataframe com 1 coluna só)
#vendas_df[0] -> NÃO FUNCIONA ASSIM PARA DATAFRAMES
#vendas_df[:3] -> pega até a linha de índice 3 do dataframe
#vendas_df[['coluna_x', 'coluna_y', 'coluna_z']] -> cria um novo dataframe com as colunas coluna_x, coluna_y e coluna_z
#vendas_df['coluna_x'][0] -> pega o itemd a 1ª linha da coluna coluna_x

import pandas as pd

# r para indicar texto bruto
vendas_df = pd.read_csv(r"E:\basesDados\Contoso - Vendas - 2017.csv", sep=";") # com o separador
lojas_df = pd.read_csv(r"E:\basesDados\Contoso - Lojas.csv", sep=";")
produtos_df = pd.read_csv(r"E:\basesDados\Contoso - Cadastro Produtos.csv", sep=";")
clientes_df = pd.read_csv(r"E:\basesDados\Contoso - Clientes.csv", sep=";")

#print(vendas_df["Quantidade Vendida"])
print(vendas_df["ID Produto"][0]) #pegar o item especicamente

vendas_df.info() #para entender a base, dar uma visão geral para poder tratar.

listaClientes = vendas_df["ID Cliente"]

#dataframe de vendas, filtrado
lista_col1 = ["ID Produto", "Quantidade Vendida", "Quantidade Devolvida"]
produtos_qtd_vendas = vendas_df[lista_col1]
print(produtos_qtd_vendas)

#imprime o dataframe
#print(vendas_df)



