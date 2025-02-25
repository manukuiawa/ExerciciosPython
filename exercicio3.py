'''
Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de
reajuste. Calcular e escrever o valor do novo salário.
'''

#ler o salário
#ler o reajuste
#calcular o reajuste
#printar o salário atual

salario = 3500
percentual_reajuste = 5
reajusteSalarial = salario * (percentual_reajuste / 100)
salarioReajustado = salario + reajusteSalarial

print(f'O seu novo salário com os devidos reajustes é de: {salarioReajustado:.0f} reais')
