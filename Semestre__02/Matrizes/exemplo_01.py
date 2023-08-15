import random
# Criar uma matriz
def criaMatriz(x):
    i = j = x
    matriz = []
    for n in range(0,j):
        matriz.append([0]*i)
    return matriz


# Criar uma matriz de números aleatórios
def criaMatrizDeNumerosAleatórios(x):
    matrizaleatoria = lista(x)
    for n in range(len(matrizaleatoria)):
        for j in range(len(matrizaleatoria[0])):
            matrizaleatoria[n][j] += random.randint(-10,10)
    return matrizaleatoria


# Exibir uma maztriz
def exibirmatriz(matriz):
    for i in matriz:
        print(i)
    print("\n")
        

# Somar um número a uma matriz
def somarUmNumeroAumaMatriz(matriz,numero):
    for n in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[n][j] += numero
    return matriz


# Soma duas matrizes
def somaMatrizes(matriz_1,matriz_2):
    if len(matriz_1) == len(matriz_2) and len(matriz_1[0]) == len(matriz_2[0]):
        for i in range(len(matriz_1)):
            for j in range(len(matriz_1[i])):
                matriz_1[i][j] += matriz_2[i][j]
        return matriz_1
    else:
        print("Matrizes com dimensões diferentes, portanto não podem ser somadas")




#somar um número a uma matriz
# somarUmNumeroAumaMatriz(matriz,10)


# Cria uma matriz de 0
matriz0 = lista(3)

# cria uma matriz de números aleatórios com dimensão definida
matriz1 = listaAleatória(3)
matriz2 = listaAleatória(3)


exibirmatriz(matriz0)
exibirmatriz(matriz1)
exibirmatriz(matriz2)


matrizSomanda = somaMatrizes(matriz1,matriz2)

exibirmatriz(matrizSomanda)


