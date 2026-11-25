#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int jumpHeight, numberPipes;
    cin >> jumpHeight >> numberPipes;

    int currentHeight;
    cin >> currentHeight;

    bool response = true;
    for(size_t i = 1; i < numberPipes; i++){
        int pipeHeight;
        cin >> pipeHeight;

        if(abs(pipeHeight - currentHeight) <= jumpHeight){
            currentHeight = pipeHeight;
            continue;
        }
        
        response = false;
        break;
    }
    
    cout << (response ? "YOU WIN\n" : "GAME OVER\n");
}