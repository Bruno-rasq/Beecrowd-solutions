#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
using namespace std;

// PROBLEMA PEDE PARA IDENTIFICAR SE UM DADA SEQUÊNCIA DE ENTRADA DE
// DADOS E SAIDA REPRESENTA UMA PILHA, FILA, FILA PRIORITÁRIA, SEM 
// CERTEZA OU ESTRUTURA IMPOSSÍVEL.

// FILA: (FIFO - FIRST IN FIRST OUT) O PRIMEIRO QUE ENTRA É O PRIMEIRO
// QUE SAI.

// STACK: (LIFO - LAST IN FIRST OUT) O ÚLTIMO A ENTRAR É O PRIMEIRO A
// SAIR.

// PRIORITY QUEUE: O ELEMENTO DE MAIOR PRIORIDADE DEVE SAIR PRIMEIRO.

int main() {

    int n;
    while(cin >> n) {

        queue<int> QUEUE;
        stack<int> STACK;
        priority_queue<int> PRIORITY_Q;

        unordered_map<string, bool> predictions = {
            {"queue", true},
            {"stack", true},
            {"priority", true},
        };

        while(n--){
            
            int operation, value;
            cin >> operation >> value;

            switch(operation){
                default: { break; }
                
                case 1: {
                    QUEUE.push(value);
                    STACK.push(value);
                    PRIORITY_Q.push(value);
                    break;
                }
                
                case 2: {
                    
                    if(!QUEUE.empty()){
                        int OUT = QUEUE.front();
                        if(OUT == value) QUEUE.pop();
                        else predictions["queue"] = false;
                    } else
                        predictions["queue"] = false;

                    if(!STACK.empty()){
                        int OUT = STACK.top();
                        if(OUT == value) STACK.pop();
                        else predictions["stack"] = false;
                    } else 
                        predictions["stack"] = false;
                    
                    if(!PRIORITY_Q.empty()){
                        int OUT = PRIORITY_Q.top();
                        if(OUT == value) PRIORITY_Q.pop();
                        else predictions["priority"] = false;
                    } else 
                        predictions["priority"] = false;

                    break;
                }
            }
        }

        if(predictions["stack"] && !predictions["queue"] && !predictions["priority"])
            cout << "stack\n";
    
        else if(!predictions["stack"] && predictions["queue"] && !predictions["priority"])
            cout << "queue\n";
        
        else if(!predictions["stack"] && !predictions["queue"] && predictions["priority"])
            cout << "priority queue\n";
            
        else if(!predictions["stack"] && !predictions["queue"] && !predictions["priority"])
            cout << "impossible\n";
            
        else
            cout << "not sure\n";
    }

    return 0;
}