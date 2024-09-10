n = int(input("Digite um número: "))
for x in range(0, n+1):
    if x % 2 != 0:#or x % 2 == 1
        print(f"{x} é um número ímpar.")