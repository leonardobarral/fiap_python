import Imagem


(m1,m2,m3) = Imagem.getMatrizImagemColorida("naturezaMorta.jpg")
# print(m1)

contador = 0

for i in range(len(m1)):
    for j in range(len(m1[0])):
        if m1[i][j] >= 27 and m1[i][j] <= 29 and m2[i][j] >= 50 and m2[i][j] <= 59 and m3[i][j] >= 130 and m3[i][j] <=140:
            m1[1][j] = 255   
            m2[1][j] = 255   
            m3[1][j] = 255
            contador += 1 

print(contador)

Imagem.salvaImagemColorida("naturezamorta2.jpg",m1,m3,m2)