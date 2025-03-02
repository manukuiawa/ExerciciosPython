'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se 
forem compradas pelo menos 12. Escreva um programa que leia O número de maçãs 
compradas, calcule e escreva O custo total da compra.
'''

preço_duzia = 1
preço_menos_duzia = 1.3
qtd_maçã = 5

if qtd_maçã >= 12 :
    preço = (qtd_maçã * preço_duzia)
else: 
    preço = (qtd_maçã * preço_menos_duzia)

print(f"Valor Total: {preço}")