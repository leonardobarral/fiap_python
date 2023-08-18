import Imagem

def pinta_branco(mat,i,j):
    lin = len(mat)
    col = len(mat[0])
        
    mat[i][j] = 255
    
    # 1º
    if i > 0 and j>0:
        mat[i-1][j-1] = 255
    
    # 2º
    if i> 0:
        mat[i-1][j] = 255
    
    # 3º
    if i > 0 and j < col -1:
        mat[i-1][j+1] = 255
    
    # 4º
    if j > 0:
        mat[i][j-1] = 255
    
    # 5º    
    if j < col-1:
        mat[i][j+1] = 255
    
    # 6º
    if i < lin - 1 and j>0:
        mat[i+1][j-1] = 255
        
    # 7º
    if i < lin - 1:
        mat[i+1][j] = 255
        
    # 8º
    if i < lin - 1 and j < col-1:
        mat[i+1][j+1] = 255


imput = Imagem.getMatrizImagemCinza("gato.jpg")

lin = len(imput)

col = len(imput[0])

output = []

for i in range(lin):
    output.append([0]*col)
    for j in range(col):
        output[i][j]= imput[i][j]
        
for i in range(lin):
    for j in range(col):
        if imput[i][j] == 255:
            pinta_branco(output,i,j)

Imagem.salvaImagemCinza("yao.jpg",output)