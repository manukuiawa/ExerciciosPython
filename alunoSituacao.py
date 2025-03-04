print("Sistema de Alunos")
aluno = input("Insira o nome do aluno(a): ")

n1 = float(input("Insira a nota da Primeira Prova: "))
n2 = float(input("Insira a nota da Segunda Prova: "))
n3 = float(input("Insira a nota da Terceira Prova: "))
n4 = float(input("Insira a nota da Quarta Prova: "))

aulaTotal = int(input("Insira quantas aulas totais teve nesse semestre: "))
aulaAluno = int(input(f"Insira quantas aulas o aluno(a) compareceu: "))

frequencia = (aulaAluno * 100) / aulaTotal

media = (n1 + n2 + n3 + n4) / 4

print(f"\nResumo do aluno(a) {aluno}:\nMédia: {media:.1f}\nFrequência: {frequencia:.0f}%")

if media >= 7 and frequencia >= 75: 
    print("Situação: Aprovado")
else: 
    print("Situação: Reprovado")