opcao = 1
while opcao == 1:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print(f"{n} é par.")
    else:
        print(f"{n} é ímpar.")
    if n < 0:
        print(f"{n} é negativo.")
    else:
        print(f"{n} é positivo.")
    opcao = int(input("Deseja continuar?\n"
                      "1 para SIM.\n"
                      "2 para NÃO."))