'''
O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem
do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do
distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de
fábrica de um carro, calcular e escrever o custo final ao consumidor.
'''
# Ler o custo de fábrica.
# Calcular o custo do distribuidor.
# Calcular o custo dos impostos.
# Calcular o custo final ao consumidor.
# Exibir o custo final.

CarroValorFabrica = 45000
CustoDistribuidor = CarroValorFabrica * (28 / 100)
impostos = CarroValorFabrica * (45 / 100)
CustoFinal = CarroValorFabrica + CustoDistribuidor + impostos

print(f'O custo final do carro é de {CustoFinal:.2f} reais')

