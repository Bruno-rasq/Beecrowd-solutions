#include <iostream>
#include <vector>
using namespace std;

vector<int> RAM(100, 0);
vector<int> stack;


/*
    COMANDOS:
    push_value -> adiciona value na stack
    push_Rpos -> adiciona o valor de R3 da RAM na stack
    pop_Rpos -> remove o top da stack e adiciona em Rpos da RAM
*/

void executeArithmeticCommand(string command){
    int x = stack.back(); stack.pop_back();
    int y = stack.back(); stack.pop_back();

    if (command == "add") stack.push_back(y + x);
    else if (command == "sub") stack.push_back(y - x);
    else if (command == "mul") stack.push_back(y * x);
    else if (command == "div") stack.push_back(y / x);
}

int main(){
    int numberOfCommands;
    cin >> numberOfCommands;

    for(int i = 0; i < numberOfCommands; i++){
        string cmd;
        cin >> cmd;

        if(cmd.rfind("push_R", 0) == 0) {
            int pos = stoi(cmd.substr(6));
            stack.push_back(RAM[pos]);
        }
        else if(cmd.rfind("push_", 0) == 0){
            int value = stoi(cmd.substr(5));
            stack.push_back(value);
        }
        else if(cmd.rfind("pop_R", 0) == 0){
            int pos = stoi(cmd.substr(5));
            int value = stack.back(); stack.pop_back();
            RAM[pos] = value;
        }
        else if(cmd == "print"){
            int value = stack.back(); stack.pop_back();
            cout << value << endl;
        }
        else {
            executeArithmeticCommand(cmd);
        }
    }
}