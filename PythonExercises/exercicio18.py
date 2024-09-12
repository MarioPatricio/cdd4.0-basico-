soma = 0
n = 1
quant = int(input("Digite a quantidade de alunos: "))
while n <= quant:
    nota = int(input(f"A soma é {soma}. Digite a nota do aluno {n}: "))
    soma = soma + nota
    n += 1
media = soma/quant
print(f"A média geral é {media}")