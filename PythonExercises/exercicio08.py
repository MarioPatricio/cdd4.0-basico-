time1 = input("Digite o nome do time: ")
gol1 = int(input("Digite a quantidade de gols: "))
time2 = input("Digite o nome do time: ")
gol2 = int(input("Digite a quantidade de gols: "))
if gol1 > gol2:
    print(f"O {time1} é o vencedor.")
elif gol1 == gol2:
    print(f"O jogo deu empate.")
else:
    print(f"O {time2} é o vencedor.")