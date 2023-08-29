import random

#criar um tabuleiro
def criaTabuleiro(d):
    i=j=d
    tabuleiro = []
    for n in range(i):
        tabuleiro.append([" "]*j)
    return tabuleiro

#inclui as bombas no tabuleiro
def incluiBombas(tabuleiro):
    nElementos = len(tabuleiro)*len(tabuleiro[0])
    posicaoDasBombas = [];
    while len(posicaoDasBombas)< len(tabuleiro):
        numi = random.randint(0,len(tabuleiro)-1)
        numj = random.randint(0,len(tabuleiro[0])-1)
        if tabuleiro[numi][numj] != "X":
            tabuleiro[numi][numj] = "x"
            posicaoDasBombas.append((numi,numj))
    return tabuleiro

def verificaVizinhaca(tabuleiro,i,j):
    contador = 0

    if tabuleiro[i][j] != "x":
        if tabuleiro[i-1][j-1] == "x":
            contador +=1
        if tabuleiro[i-1][j] == "x":
            contador +=1
        if tabuleiro[i-1][j+1] == "x":
            contador +=1
        if tabuleiro[i+1][j-1] == "x":
            contador +=1
        if tabuleiro[i+1][j] == "x":
            contador +=1
        if tabuleiro[i+1][j+1] == "x":
            contador +=1
        if tabuleiro[i][j-1] == "x":
            contador +=1
        if tabuleiro[i][j+1] == "x":
            contador +=1
        tabuleiro[i][j]= str(contador)

    return tabuleiro


# Jogada
def joga(i,j,tabuleiro):
    if tabuleiro[i][j]=="x":
        print("Perdeu")
        return -1
    else:
        
        tabuleiro = verificaVizinhaca(tabuleiro,i-1,j-1)
        tabuleiro = verificaVizinhaca(tabuleiro,i-1,j)
        tabuleiro = verificaVizinhaca(tabuleiro,i-1,j+1)
        tabuleiro = verificaVizinhaca(tabuleiro,i+1,j-1)
        tabuleiro = verificaVizinhaca(tabuleiro,i+1,j)
        tabuleiro = verificaVizinhaca(tabuleiro,i+1,j+1)
        tabuleiro = verificaVizinhaca(tabuleiro,i,j-1)
        tabuleiro = verificaVizinhaca(tabuleiro,i,j+1)
        # tabuleiro[i][j] = "#"

    return tabuleiro

        


#exibir o tabuleiro
def exibiTabuleiro(tabuleiro):
    for i in tabuleiro:
        print(i)
    print("\n")


