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
campo_jogo_player = [
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
]
campo_jogo_ia = [
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
]


def verificacao(valor):
    if valor == 0:
        return True
    return False


def verificarVazio(elemento, x, y, vetor):
    cont = 0
    try:
        for i in range(0, elemento[0]):
            if verificacao(vetor[x][y + i]) == True:
                cont += 1
            if cont == elemento[0]:
                return True
            if cont > elemento[0]:
                return False
    except:
        return False


def verificarTamanho(elemento, posicao):
    if elemento[0] + posicao > 8:
        return False
    return True


# * Gerar valores aleatórios
def coluna_aleatorio():
    return random.randint(0, colunas - 1)


def linha_aleatorio():
    return random.randint(0, linhas - 1)


# * Adicionar elementos
def add_elemento(elemento, vetor, linha, coluna):
    for j in range(0, elemento[0]):
        vetor[linha][coluna + j] = elemento[0]


# * Posicionar elemento
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


def inicializacao(vetor):
    contador = 0
    while contador <= (
        submarino[1] + contratorpedeiro[1] + navio_tanque[1] + porta_avioes[1]
    ):
        i = coluna_aleatorio()
        j = linha_aleatorio()
        if verificacao(vetor[i][j]) == True:
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


def posi_elem_jogador(vetor):
    contador = 0
    while contador <= (
        submarino[1] + contratorpedeiro[1] + navio_tanque[1] + porta_avioes[1]
    ):
        print(campo_jogador1)
        if contador < 2:
            print("escolha a casa para posicionar o submarino")
            i = int(input("escolha a linha: "))
            j = int(input("escolha a coluna: "))
            if verificacao(vetor[i][j]) == True:
                if verificarTamanho(submarino, j) == True:
                    if verificarVazio(submarino, i, j, vetor) == True:
                        posicionar_sub(submarino, vetor, i, j)
                        contador += 1
                    else:
                        print(
                            "Já tem outro elemento em alguma casa que o submarino vai entrar"
                        )
                else:
                    print("o submarino não vai caber nessa posição")
            else:
                print("Já tem um elemento nessa posição")
        elif contador < 3:
            print("escolha a casa para posicionar o contratorpedeiro")
            i = int(input("escolha a linha: "))
            j = int(input("escolha a coluna: "))
            if verificacao(vetor[i][j]) == True:
                if verificarTamanho(contratorpedeiro, j) == True:
                    if verificarVazio(contratorpedeiro, i, j, vetor) == True:
                        posicionar_contratorpedeiro(contratorpedeiro, vetor, i, j)
                        contador += 1
                    else:
                        print(
                            "Já tem outro elemento em alguma casa que o submarino vai entrar"
                        )
                else:
                    print("o submarino não vai caber nessa posição")
            else:
                print("Já tem um elemento nessa posição")
        elif contador < 4:
            print("escolha a casa para posicionar o navio tanque")
            i = int(input("escolha a linha: "))
            j = int(input("escolha a coluna: "))
            if verificacao(vetor[i][j]) == True:
                if verificarTamanho(navio_tanque, j) == True:
                    if verificarVazio(navio_tanque, i, j, vetor) == True:
                        posicionar_navio_tanque(navio_tanque, vetor, i, j)
                        contador += 1
                    else:
                        print(
                            "Já tem outro elemento em alguma casa que o submarino vai entrar"
                        )
                else:
                    print("o submarino não vai caber nessa posição")
            else:
                print("Já tem um elemento nessa posição")
        elif contador < 5:
            print("escolha a casa para posicionar o porta aviões")
            i = int(input("escolha a linha: "))
            j = int(input("escolha a coluna: "))
            if verificacao(vetor[i][j]) == True:
                if verificarTamanho(porta_avioes, j) == True:
                    print("chegou aqui")
                    if verificarVazio(porta_avioes, i, j, vetor) == True:
                        print("Entrou aqui")
                        posicionar_porta_avioes(porta_avioes, vetor, i, j)
                        contador += 1
                    else:
                        print(
                            "Já tem outro elemento em alguma casa que o submarino vai entrar"
                        )
                else:
                    print("o submarino não vai caber nessa posição")
            else:
                print("Já tem um elemento nessa posição")
        else:
            print(vetor)
            break


def printarVetor(vetor, col):
    print("   ", end="", flush=True)
    for i in range(0, col):
        print(i+1," ", end="",flush=True)
    print("", flush=True)
    for count, vetor in enumerate(vetor):
        print(count+1, vetor)

def jogo():
    posi_elem_jogador(campo_jogador1)
    inicializacao(campo_ia)
    vez_player = True
    vez_ia = False
    turnos = 1
    pontos_player = 0
    pontos_ia = 0
    while (pontos_player or pontos_ia) < 10:
        while vez_player == True:
            print("-" * 30, "\n", "turno: ", turnos)
            print("Coordenadas disparadas")
            printarVetor(campo_jogo_player, colunas)
            print("escolha a casa para disparar!")
            i = int(input("escolha a linha: "))
            j = int(input("escolha a coluna: "))
            if i<8 and j<8:
                if campo_ia[i][j] != 0:
                    print("você acertou")
                    campo_jogo_player[i][j] = "X"
                else:
                    print("Você errou")
                    campo_jogo_player[i][j] = "O"
                    vez_player = False
                    vez_ia = True
                turnos += 1
            else:
                print("valores de Coordenadas inválidos")
        while vez_ia == True:
            print("-" * 30, "\n", "turno: ", turnos)
            print("É a vez da IA")
            i = linha_aleatorio()
            j = coluna_aleatorio()
            if i<8 and j<8:
                if campo_jogador1[i][j] != 0:
                    print("O bot acertou uma embarcação")
                    campo_jogo_ia[i][j] = "X"
                else:
                    print("O bot errou")
                    campo_jogo_ia[i][j] = "O"
                    vez_player = True
                    vez_ia = False
                turnos += 1
            else:
                print("valores de Coordenadas inválidos")


jogo()
