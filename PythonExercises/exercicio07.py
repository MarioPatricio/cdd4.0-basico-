n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
media = (n1+n2+n3)/3
if media >= 7:
    print("Aprovado com média {}.".format(media))
else:
    if media >= 4:
        print("Reprovado com média {}, poderá fazer Final.".format(media))
    else:
        print("Reprovado com média {}, sem Final.".format(media))