peso = float(input("Digite seu peso: "))
h = float(input("Digite sua altura: "))
imc = peso/(h)**2
print(f"Seu IMC é {imc:.2f}.")
if imc < 18.6:
    print("Abaixo do peso.")
else:
    if imc >= 18.6 and imc < 25:
        for x in range(600):
            print("Peso ideal. PARABÉNS!")
    if imc >= 25 and imc < 30:
        print("Levemente acima do peso.")
    if imc >= 30 and imc < 35:
        print("Obesidade grau I.")
    if imc >= 35 and imc < 40:
        print("Obesidade grau II, severa.")
    if imc >= 40:
        print("Obesdidade grau III, mórbida.")