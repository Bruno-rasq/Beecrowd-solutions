#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define BUFFER stringstream
#define IMAGE vector<string>

// DECLARA IMAGEM GLOBALMENTE.
IMAGE image;

// DESCOBRIR SE UM QUADRANTE É UNIFORME.
// CASO SIM RETORNA QUAL O PIXEL FORMA O QUADRANTE W/B
// CASO CONTRÁRIO INPRIME UM Q E DIVIDE K QUADRANTE EM
// 4 OUTROS QUADRANTES RECURSIVAMENTE.
void COMPRESS(int x, int y, int size, BUFFER& OUT){
    char top_left_pixel = image[x][y];
    bool same_pixel = true;
    for (int i = x; i < x + size; i++) {
        for (int j = y; j < y + size; j++) {
            if (image[i][j] != top_left_pixel) {
                same_pixel = false;
                break;
            }
        }
        if (!same_pixel) break;
    }

    if (same_pixel) {
        OUT << top_left_pixel;
        return;
    }

    OUT << 'Q';
    int half = size / 2;
    COMPRESS(x,        y,        half, OUT);
    COMPRESS(x,        y + half, half, OUT);
    COMPRESS(x + half, y,        half, OUT);
    COMPRESS(x + half, y + half, half, OUT);
}

int main() {

    string line;
    // PRIMEIRA LINHA:
    // #define quadtree_width N
    getline(cin, line);

    BUFFER ss(line);

    string lixo;
    int N;
    ss >> lixo >> lixo >> N;

    // #define quadtree_height N
    getline(cin, line);

    // static char quadtree_bits[] = {
    getline(cin, line);

    // IMAGEM N x N
    image.resize(N, string(N, 'W'));

    // LÊ AS N LINHAS DA IMAGEM
    for (int y = 0; y < N; y++) {
        getline(cin, line);

        // Troca ',' por espaço
        for (char& c : line)
            if (c == ',') c = ' ';

        BUFFER ss(line);

        // Cada hexadecimal representa 8 pixels
        for (int x = 0; x < N; x += 8) {
            unsigned int value;
            ss >> hex >> value;
            for (int bit = 0; bit < 8; bit++) {
                image[y][x + bit] =
                    ((value >> bit) & 1) ? 'B' : 'W';
            }
        }
    }

    BUFFER OUT;
    OUT << N << "\n";

    // COMPRIME A IMAGEM INTEIRA
    COMPRESS(0, 0, N, OUT);

    cout << OUT.str() << "\n";

    return 0;
}