'''
Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por 
mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas 
por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor 
total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e 
escreva o salário final do vendedor.
'''

salarioFixo = 2000
valorPorCarro = 100
valorDasVendas = 100000
qtdCarroVendido = 12

totalComissao = (qtdCarroVendido * valorPorCarro)
bonus = (valorDasVendas * 5) / 100

salarioFinal = (salarioFixo + totalComissao + bonus)

print(f'Salário Final: R${salarioFinal:.2f} reais')

