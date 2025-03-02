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

