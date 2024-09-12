n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
while n1 >= n2:
    n1 = int(input("Valor inválido! N1 deve ser menor que n2: "))
for x in range(n1, n2, 1):
    print(x, end = " ")
for x in range(n2, n1-1, -1):
    print(x, end = " ")