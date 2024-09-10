soma = 0
quant = int(input("Digite a  quantidade de alunos: "))
for x in range(quant):
    a = float(input(f"Digite a nota do aluno {x}: "))
    soma = soma + a
media = soma/quant
print(f"A soma de todas as notas é {soma}")
print(f"A média geral é: {media}")