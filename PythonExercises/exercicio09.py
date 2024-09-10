quant = float(input("Quantos litros? "))
print("Gasolina está R$5,80 o litro e Etanol, R$4,90")
G = 5.8 * quant #lembrar de calcular dentro dos booleanos, para consumir menos memória
E = 4.9 * quant
tipo = input("Digite G para Gasolina e E para Etanol: ")
if tipo == "G" or tipo == "g":
    print(f"O valor a ser pago é R${G:,2f}")
elif tipo == "E" or tipo == "e":
    print(f"O valor a ser pago é R${E:,2f}")
else:
    print("Combustível inválido.")