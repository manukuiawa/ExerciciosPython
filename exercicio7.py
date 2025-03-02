'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se 
forem compradas pelo menos 12. Escreva um programa que leia O número de maçãs 
compradas, calcule e escreva O custo total da compra.
'''
print("Bem vindo ao Sistema de Compras!")
nome = input("Insira seu nome para iniciar o atendimento: ")
print(f'Olá {nome}, vamos lá.')

continuar = 'sim'

while(continuar.lower() == "sim"):

    qtd_maça = int(input("Insira a quantidade de maçãs: "))
    
    adicionarSacola = input("Deseja adicionar mais maçãs em sua sacola? (sim/não)")

    if adicionarSacola.lower() == 'sim':
        qtdMais = input("Quantas?")

    else: 
         continue
    
    totalMaçãs = qtd_maça + qtdMais

    decisaoPagamento = input("Deseja ir para o pagamento? (sim/não)")
    
    preço = 1.00 if qtd_maça >= 12 else 1.30
    totalCompra = (qtd_maça * preço)
    
    resumoCompra = print(f'Resumo da Compra: \nMaçãs: {totalMaçãs}\nValor: R${totalCompra:.2f}')
    formaPagamento = input("Qual a forma de pagamento? (D = debito/ P = Pix)").lower()

    print("Processando...")
    print("Pagamento Aprovado!")

    continuar = input("Deseja realizar outra compra? (Sim/Não)")

print(f'Obrigado {nome}! Volte sempre.')



#erro 1 -> quando coloca nao, o programa continua - 
#erro 2-> deseja ir para o pagamento, quando dizer nçao volte no deseja adicionar mais maçãs
#erro 3 -> quando coloca deseja ir para o pagamento, não reconhece sim/nao