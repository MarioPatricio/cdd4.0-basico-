soma = 0
for i in range(10):
    n = int(input("Digite um número ÍMPAR: "))
    if n % 2 != 0:
        soma = soma + n
print(f"{soma}")