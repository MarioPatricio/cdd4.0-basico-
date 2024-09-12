opcao = 1
while opcao == 1:
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("Digite o 2º número: "))
    while n2 == 0:
            n2 = int(input("Digite um número diferente de zero: "))
    div = n1/n2
    print(f"A divisão entre {n1} e {n2} é {div}.")
    opcao = int(input("Deseja continuar? \n"
                  "1 para sim.\n"
                  "2 para não.\n"))
