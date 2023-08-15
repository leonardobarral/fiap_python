
def criaMatriz(dimensao):
    i = j = x
    matriz = []
    for n in range(0,j):
        matriz.append(['']*i)
    return matriz

def exibiMatriz(matriz):
    for i in matriz:
        print(i)
    print("\n")

def temEspaco(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == "":
                return True
    return False

def joga(matriz,lin,col,jogador):
    if matriz[lin][col] == "":
        matriz[lin][col] = jogador
        return True
    else:
        return False

def haGanhador(m):
    # Verificando as Linhas
    for i in range(3):
        if m[i][0] == m[i][1] and m[i][1] == m[i][2] and m[i][0] !="":
            return True
    # Verificando as colunas
    for j in range(3):
        if m[0][j] == m[1][j] and m[1][j] == m[2][j] and m[0][j] !="":
            return True
    
    # Verificando a 1º diagoal
    for d in range(3):
        if m[0][0] == m[1][1] and m[1][1] == m[2][2] and m[0][0] !="":
            return True
            
    # Verificando a 2º diagoal
    for d in range(3):
        if m[0][2] == m[1][1] and m[1][1] == m[2][0] and m[0][2] !="":
            return True
    return False 

