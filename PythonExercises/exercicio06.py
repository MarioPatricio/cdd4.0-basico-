n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
if n1 == n2:
    print("Os números são iguais.")
else:
    if n1 > n2:
        print("{} é maior que {}.".format(n1, n2))
    else:
        print("{} é maior que  {}.".format(n2, n1))