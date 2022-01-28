import random
import numpy as np

linhas = 8
colunas = 8

submarino = [2, 2]
contratorpedeiro = [3, 1]
navio_tanque = [4, 1]
porta_avioes = [5, 1]

campo_jogador1 = np.zeros([linhas, colunas])
campo_ia = np.zeros([linhas, colunas])


def inicializacao(vetor):
    contador = 0
    while contador <= (
        submarino[1] + contratorpedeiro[1] + navio_tanque[1] + porta_avioes[1]
    ):
        i = coluna_aleatorio()
        j = linha_aleatorio()
        if verificacao(vetor[i][j]):
            if contador < 2:
                if verificarTamanho(submarino, j) == True:
                    if verificarVazio(submarino, i, j, vetor) == True:
                        posicionar_sub(submarino, vetor, i, j)
                        contador += 1
            elif contador < 3:
                if verificarTamanho(contratorpedeiro, j) == True:
                    if verificarVazio(contratorpedeiro, i, j, vetor) == True:
                        posicionar_contratorpedeiro(contratorpedeiro, vetor, i, j)
                        contador += 1
            elif contador < 4:
                if verificarTamanho(navio_tanque, j) == True:
                    if verificarVazio(navio_tanque, i, j, vetor) == True:
                        posicionar_navio_tanque(navio_tanque, vetor, i, j)
                        contador += 1
            elif contador < 5:
                if verificarTamanho(porta_avioes, j) == True:
                    if verificarVazio(porta_avioes, i, j, vetor) == True:
                        posicionar_porta_avioes(porta_avioes, vetor, i, j)
                        contador += 1
            else:
                break


def verificacao(valor):
    if valor == 0:
        return True
    return False


def verificarVazio(elemento, x, y, vetor):
    for i in range(0, elemento[0]):
        if verificacao(vetor[x][y]) != True:
            return False
    return True


def verificarTamanho(elemento, posicao):
    if elemento[0] + posicao > 8:
        return False
    return True


def coluna_aleatorio():
    return random.randint(0, colunas - 1)


def linha_aleatorio():
    return random.randint(0, linhas - 1)


def add_elemento(elemento, vetor, linha, coluna):
    for j in range(0, elemento[0]):
        vetor[linha][coluna + j] = elemento[0]


def posicionar_sub(elemento, vetor, linha, coluna):
    i = 0
    for i in range(0, elemento[1]):
        add_elemento(elemento, vetor, linha, coluna)


def posicionar_contratorpedeiro(elemento, vetor, linha, coluna):
    i = 0
    for i in range(0, elemento[1]):
        add_elemento(elemento, vetor, linha, coluna)


def posicionar_navio_tanque(elemento, vetor, linha, coluna):
    i = 0
    for i in range(0, elemento[1]):
        add_elemento(elemento, vetor, linha, coluna)


def posicionar_porta_avioes(elemento, vetor, linha, coluna):
    i = 0
    for i in range(0, elemento[1]):
        add_elemento(elemento, vetor, linha, coluna)


def playerPoisionar(vetor):
    todosElementosPosicionador = False
    elementosPosicionados = [0, 0, 0, 0]
    while todosElementosPosicionador != True:
        if elementosPosicionados[0] == 0 or elementosPosicionados[0] == 1:
            print("digite linha onde onde deseja posicionar o submarino")
            linha = input(int())
            print("Digite a coluna onde deseja posicionar o submarino")
            coluna = input(int())
            if verificacao(vetor[linha][coluna]) == True:
                if verificarSubmarino() == True:
                    if verificarExistenciaDeOutros == True:
                        pisicionar_Submarino(linha, coluna, vetorJogador)
                        elementosPosicionados[0] += 1
        elif elementosPosicionados[1] == 0:
            print("digite linha onde onde deseja posicionar o Contratorperdeira")
            linha = input(int())
            print("Digite a coluna onde deseja posicionar o Contratorperdeira")
            coluna = input(int())
            if verificacao(vetor[linha][coluna]) == True:
                if verificarEspaco() == True:
                    if verificarExistenciaDeOutros == true:
                        pisicionar_navio(linha, coluna, vetorJogador)
                        elementosPosicionados[1] += 1

        elif elementosPosicionados[2] == 0:
            print("digite linha onde onde deseja posicionar o Navio Tanque ")
            linha = input(int())
            print("Digite a coluna onde deseja posicionar o Navrio Tanque ")
            coluna = input(int())
            if verificacao(vetor[linha][coluna]) == True:
                if verificarEspaco() == True:
                    if verificarExistenciaDeOutros == true:
                        pisicionar_navio(linha, coluna, vetorJogador)
                        elementosPosicionados[2] += 1

        elif elementosPosicionados[3] == 0:
            print("digite linha onde onde deseja posicionar o Porta-Aviões ")
            linha = input(int())
            print("Digite a coluna onde deseja posicionar o Porta-Aviões ")
            coluna = input(int())
            if verificacao(vetor[linha][coluna]) == True:
                if verificarEspaco() == True:
                    if verificarExistenciaDeOutros == True:
                        pisicionar_navio(linha, coluna, vetorJogador)
                        elementosPosicionados[3] += 1

