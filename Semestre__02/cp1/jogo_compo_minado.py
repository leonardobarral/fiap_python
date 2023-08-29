import campo_minado

dimensaoTabuleiro = int(input("Dimensão do Tabuleiro: "))

tabuleiro = campo_minado.criaTabuleiro(dimensaoTabuleiro)

campo_minado.exibiTabuleiro(tabuleiro)

tabuleiro = campo_minado.incluiBombas(tabuleiro)

campo_minado.exibiTabuleiro(tabuleiro)

campo_minado.joga(5,5,tabuleiro)

campo_minado.exibiTabuleiro(tabuleiro)