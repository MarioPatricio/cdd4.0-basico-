opcao = 1
while opcao == 1: # ou opcao != 2:
    n1 = float(input("Digite a 1º nota: "))
    while n1 < 0 or n1 > 10:
        n1 = float(input("Digite a 1º nota novamente: "))
    n2 = float(input("Digite a 2º nota: "))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Digite a 2º nota novamente: "))

    media = (n1+n2)/2
    if media < 4:
        print("Aluno reprovado.")
    else:
        if media >= 4:
            print("Aluno em recuperação.")
        if media >= 7:
            print("Aluno aprovado.")

    print(f"Aluno com média: {media}")
    opcao = int(input("Deseja continuar? \n"
                      "1 para sim.\n"
                      "2 para não.\n"))