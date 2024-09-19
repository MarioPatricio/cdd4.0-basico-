rep = 1
while rep == 1:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    print("Digite\n"
          f"1 --> Soma\n"
          f"2 --> Subtração\n"
          f"3 --> Multiplicação\n"
          f"4 --> Divisão\n"
          f"5 --> Digitar um novo número\n"
          f"6 --> Sair")
    opcao = int(input("Qual operação você deseja realizar? "))
    while opcao < 1 or opcao > 6:
        opcao = int(input("Opção inválida, digite novamente:  "))
    match opcao:
        case 1:
            print("--Soma--")
            soma = n1 + n2
            print(soma)
        case 2:
            print("--Subtração--")
            sub = n1 - n2
            print(sub)
        case 3:
            print("--Multiplicação--")
            mult = n1 * n2
            print(mult)
        case 4:
            print("--Divisão--")
            while n2 == 0:
                n2 = int(input("Digite um número diferente de zero: "))
            div = n1/n2
            print(div)
        case 5:
            print("--Digitar novo número--")
            rep = 1
        case 6:
            print("--Sair--")
            rep = 0
            exit()