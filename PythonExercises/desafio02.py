senha = 1234
rep = 0
cont = 3
tent = int(input("Digite a senha: "))
while tent != senha:
    tent = int(input(f"Senha incorreta, tente mais {cont} vezes: "))
    rep += 1
    cont -= 1
    if rep >= 3:
        print("Cartão bloqueado.")
        break
else:
    print("Login efetuado.")
    exit()