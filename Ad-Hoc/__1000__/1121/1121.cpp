#include <iostream>
#include <unordered_map>
#include <vector>
#include <utility>
using namespace std;

// Robot em um grid NxM, onde há celulas vazias, celulas bloqueadas e
// e celulas com itens, o robo começar em uma coordenada específico e
// recebe uma serie de instruções.

// D - gira 90° para direita
// E - gira 90° para esquerda
// F - avança uma unidade para frente.

// Se colidir com uma celula bloqueada ou sair dos limites do grid não 
// faz nada, no final deve retornar quantos itens ele conseguiu coletar.

const unordered_map<int, pair<int, int>> delta = {
    {0, {-1,  0}}, // norte
    {1, { 0,  1}}, // leste
    {2, { 1,  0}}, // sul
    {3, { 0, -1}}, // oeste
};

const unordered_map<char, int> rotateDelta = {
    {'D', 1}, // direita
    {'E', -1},  // esquerda
};


int main() {

    int height, width, commandslength;

    while(cin >> height >> width >> commandslength) {

        if (height == 0 && width == 0 && commandslength == 0) break;

        int face = 0;
        int x = 0;
        int y = 0;
        int ans = 0;
        vector<string> grid;
        string commands;
        string line;
    
        for(size_t i = 0; i < height; i++){
            cin >> line;
    
            for(size_t j = 0; j < width; j++){
                if(line[j] == 'N' || line[j] == 'L' || line[j] == 'S' || line[j] == 'O'){
    
                    x = i;
                    y = j;
    
                    if(line[j] == 'N') face = 0;
                    if(line[j] == 'L') face = 1;
                    if(line[j] == 'S') face = 2;
                    if(line[j] == 'O') face = 3;
                }
            }
            grid.push_back(line);
        }
    
        cin >> commands;
    
        for(char cmd: commands){
    
            // rotaciona o robo.
            if(cmd == 'D' || cmd == 'E') face = (face + rotateDelta.at(cmd) + 4) % 4;
        
            // avança no sentido que o robo está rotacionado.
            else {
                int nx = x + delta.at(face).first;
                int ny = y + delta.at(face).second;
    
                if(nx >= 0 && nx < height && ny >= 0 && ny < width && grid[nx][ny] != '#'){
                
                    if(grid[nx][ny] == '*'){
                        ans++;
                        grid[nx][ny] = '.';
                    }

                    x = nx;
                    y = ny;
                }
            }
        }
    
        cout << ans << "\n";
        
    }
    return 0;
}
