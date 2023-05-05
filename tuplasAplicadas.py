#Tuplas aplicadas.
faturamento = 0
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

#Qual foi o fautramento de vendas de iphone no dia 20/08/20
#Qual foi o produto mais vendido em unidades n odia 21/08/20


#Unpacking
data, produto, cor, capacidade, unidades, valor_unitario = vendas[0] #desmembrando da pos 0 da tupla

for item in vendas:
    data, produto, cor, capacidade, unidades, valor_unitario = item
    if produto == "iphone x" and data == "20/08/2020":
        faturamento += unidades * valor_unitario
print("O faturamento de Iphone no dia 20/08/2020 foi de {}".format(faturamento))