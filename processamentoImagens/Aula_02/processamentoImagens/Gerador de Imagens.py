import Imagem
import random

# imput = Imagem.getMatrizImagemCinza("gato.jpg")

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
            matrizaleatoria[n][j] += random.randint(0,255)
    return matrizaleatoria

imputG = criaMatrizDeNumerosAleatórios(4)
imputR = criaMatrizDeNumerosAleatórios(4)
imputB = criaMatrizDeNumerosAleatórios(4)

Imagem.salvaImagemCinza("imagemR.jpg",imputR)
Imagem.salvaImagemCinza("imagemG.jpg",imputG)
Imagem.salvaImagemCinza("imagemB.jpg",imputB)
Imagem.salvaImagemColorida("imagemRGB.jpg",imputR,imputG,imputB)