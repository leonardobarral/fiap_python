# Crie a matriz do jogo da velha abaixo e faça a impressão na tela:
# x | o |x
# o | x |
# o |   |x


import random
# Criar uma matriz
def criaMatriz(x):
    i = j = x
    matriz = []
    for n in range(j):
        matriz.append([0]*i)
    return matriz

def exibirmatriz(matriz):
    for i in matriz:
        print(i)
    print("\n")
    
matriz = criaMatriz(3)
matriz[0][0]="x"
matriz[0][1]=0
matriz[0][2]="x"
matriz[1][0]=0
matriz[1][1]="x"
matriz[2][0]=0
matriz[2][2]="x"

exibirmatriz(matriz)