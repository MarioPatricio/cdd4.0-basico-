opcao = 1
while opcao == 1:
    num = int(input("Digite um número: "))
    n = 1
    res = 1
    while n <= 10:
        print(f"{num} X {n} = {res}")
        res = num * n
        n += 1
    opcao = int(input("Deseja continuar? \n"
                  "1 para sim.\n"
                  "2 para não.\n"))
