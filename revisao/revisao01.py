a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
soma = a + b
print("A soma entre {} e {} é {}.".format(a, b, soma))
if soma > c:
    print("A soma entre {} e {} é maior do que {}.".format(a, b, c))
else:
    if soma < c:
        print("A soma entre {} e {} é menor do que {}.".format(a, b, c))
    if soma == c:
        print("A soma entre {} e {} é igual à {}.".format(a, b, c))