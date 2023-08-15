import velha

tab = velha.criaMatriz(3)

player = "x"

while velha.temEspaco(tab) and not velha.haGanhador(tab):
    velha.exibiMatriz(tab)
    print("Vez do jogador: ", player)
    lin = int(input("LInha: "))
    col = int(input("Coluna: "))
    