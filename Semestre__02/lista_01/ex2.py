# . Escreva uma função getDimensao que recebe como parâmetro uma matriz mat de números
# reais (double) e retorna uma tupla (ou uma lista) de inteiros contendo o número de linhas e
# o número de colunas de mat. Note que, sua tupla terá duas posições.
import random
import math

def criaMatriz(x):
    i = j = x
    matriz = []
    for n in range(0,j):
        matriz.append([0]*i)
    return matriz

def criaMatrizDeNumerosAleatórios(x):
    matrizaleatoria = criaMatriz(x)
    for n in range(len(matrizaleatoria)):
        for j in range(len(matrizaleatoria[0])):
            matrizaleatoria[n][j] += round(random.uniform(-10,10),1)
    return matrizaleatoria

def getDimensaos(mat):
    return (len(mat),len(mat[0]))

def exibirmatriz(matriz):
    for i in matriz:
        print(i)
    print("\n")
    return None

mat = criaMatrizDeNumerosAleatórios(8)
exibirmatriz(mat)
print("A resposta é ",getDimensaos(mat))