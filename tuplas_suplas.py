#tuplas
#sempre coloque entre parenteses....tuplas são imutaveis, muito usados para cores
# Unpacking em tuplas
cores = ("Red", "Green", "Blue", "Gray")
vermelho = cores[0]
verde = cores[1]

vendas = [1000,5000,20000,2000, 600]
funcionarios = ["Bruno", "Larissa", "Mag", "Theo", "Sophie"]
#....etc

#acessar os valores de maneira mais simples.
vermelho, verde, azul, cinza = cores

for i, venda in enumerate(vendas):
    print('{} vendeu {} unidades'.format(funcionarios[i], venda))

print(verde)
print(cores)