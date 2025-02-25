'''
Escreva um algoritmo para ler o número total de eleitores de um município, o número de
votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em
relação ao total de eleitores
'''

#ler total de eleitores
#ler total de votos brancos
#ler total de votos nulos 
#ler total de votos validos, que não pode ser maior que o total de eleitores
#fazer a porcentagem
#printar na tela

totalDeEleitores = 1000
totalVotosValidos = 650
totalVotosBrancos = 200
totalVotosNulos = 150

if (totalVotosValidos + totalVotosBrancos + totalVotosNulos >= totalDeEleitores):
    PorcentagemValidos = (totalVotosValidos / totalDeEleitores) * 100
    PorcentagemBrancos = (totalVotosBrancos / totalDeEleitores) * 100
    PorcentagemNulos = (totalVotosNulos / totalDeEleitores) * 100

    print(f'% de Votos Válidos: {PorcentagemValidos:.0f}%')
    print(f'% de Votos Brancos: {PorcentagemBrancos:.0f}%')
    print(f'% de Votos Nulos: {PorcentagemNulos:.0f}%')
else: 
    print('Votos Inválidos!')
