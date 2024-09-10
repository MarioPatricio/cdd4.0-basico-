h1 = int(input("Digite a 1º hora: "))
m1 = int(input("Digite o 1º minuto: "))
h2 = int(input("Digite a 2º hora: "))
m2 = int(input("Digite a 2º minuto: "))

if(h1 < 0 or h1 > 23) and (h2 < 0 or h2 > 23):
    print("Erro.")
    exit()
else:
    if (m1 < 0 or m1 > 59) and (m2 < 0 or m2 >59):
        print("Erro.")
        exit()

if h1 > 12 and h2 > 12:
    h1 -= 12
    h2 -= 12

htotal = h1 + h2
mtotal = m1 + m2
if mtotal >= 60:
    htotal += 1
    mtotal -= 60
if htotal > 12:
    htotal -= 12

if mtotal < 10:
    print(f"{htotal}:0{mtotal}")
else:
    print(f"{htotal}:{mtotal}")