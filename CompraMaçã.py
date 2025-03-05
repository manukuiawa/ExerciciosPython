print("Bem vindo ao Sistema de Compras!")
nome = input("Insira seu nome para iniciar o atendimento: ")
print(f'Olá {nome}, vamos lá.')

continuar = 's'

while continuar == 's':
    qtd_maçã = int(input("Insira a quantidade de maçãs: "))

    perguntaqtd_mais = input("Deseja adicionar mais na sacola? ")

    if perguntaqtd_mais == 's': 
        qtd_mais = int(input("Quantas? "))

        pagamento = input("Deseja ir para o pagamento? ")

        qtd_maçã = (qtd_maçã + qtd_mais)
        preço = 1.00 if qtd_maçã <= 12 else 1.30
        totalCompra = (qtd_maçã * preço)

        if pagamento == 's': 
            print(f"Resumo da Compra:\nQuantidade de Maçãs: {qtd_maçã}\nTotal da Compra: R${totalCompra:.2f} reais")
            
            formaPagamento = input("Insira a forma de pagamento (D = débito ou P = Pix): ")
            print("Processando...")
            print("Pagamento Aprovado!")
            break
        elif pagamento != 's': 
            print("Compra Cancelada!")
            break
    else: 
        preço = 1.00 if qtd_maçã <= 12 else 1.30
        totalCompra = (qtd_maçã * preço)
        pagamento = input("Deseja ir para o pagamento?\n ")
        print(f"Resumo da Compra:\nQuantidade de Maçãs: {qtd_maçã}\nTotal da Compra: R${totalCompra:.2f} reais")
        formaPagamento = input("Insira a forma de pagamento (D = débito ou P = Pix): ")
        print("Processando...")
        print("Pagamento Aprovado!")
        break  
            
    
print(f"Obrigado pela preferência {nome}, volte sempre!")