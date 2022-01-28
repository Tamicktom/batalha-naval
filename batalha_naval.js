// Cada jogador vai ter uma matriz que representa o campo dele;
var matrizJogador1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
];
var matrizJogador2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
];

// Quando o jogo iniciar, os jogadores vão posicionar os elementos dentro da 8x8.


// Isso se refere a quantidade de espaço que o elemento ocupa, seguido pela quantidade dele.
var submarino = [2, 2],
    contratorpedeiro = [3, 1],
    navioTanque = [4, 1],
    portaAvioes = [5, 1];

function gerarPosicioesIA() {
    pocisionarElemento(submarino);
    pocisionarElemento(contratorpedeiro);
    pocisionarElemento(navioTanque);
    pocisionarElemento(portaAvioes);
}

function pocisionarElemento(elemento) {
    var posicionarElemento = false;
    
    while (posicionarElemento != true) {
        var X = parseInt(Math.random() * 7);
        var Y = parseInt(Math.random() * 7);
        console.log(X, Y)
        //~> Procurar aleatóriamente um espaço vazio dentro da matriz, verifica se o elemento vai caber ou na horizontal ou na vertical
        if (matrizJogador2[X][Y] == 0 && verificarEspaçoHorizontal(elemento, X, Y) == true) {
            //! Posiciona o elemento na horizontal
            posicionarElemento = true;
        } else if (matrizJogador2[X][Y] == 0 && verificarEspaçoVertical(elemento, X, Y) == true) {
            //! Posiciona o elemento na vertical
            posicionarElemento = true;
        }

    }
}
function verificarEspaçoHorizontal(elemento, X, Y) {
    for (var i = 0; i < elemento[0]; i++) {
        if (matrizJogador2[X + i][Y] != null) {
            console.log("elemento pode ser posicionado em " + matrizJogador2[X + i][Y]);
        }
        if (matrizJogador2[X + i][Y] == null) {
            return false;
        }
    }
    return true;
}
gerarPosicioesIA()
console.log(matrizJogador2);