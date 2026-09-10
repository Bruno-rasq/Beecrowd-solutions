#include <iostream>
#include <stack>
#include <sstream>
#include <string>
using namespace std;

// OBJETIVO: TRANSPOR UMA EXPRESSÃO MATEMÁTICA IN-FIXA PARA POS-FIXA.

// ESTRUTURA PARA UM OPERADOR. ARMAZENA SIMBOLO E NVL DE PRECEDENCIA.
struct Operator {
    char symbol;
    int precedence;
};

#define STACK stack<Operator>
#define BUFFER stringstream

// EMPILHAR OPERADORES NA STACK.
// SE A STACK ESTIVER VAZIA, ADICIONA O OPERADOR ATUAL.
// SE O OPERADOR NO TOPO TIVER PRECEDENCIA MENOR,
// APENAS ADICIONA O NOVO OPERADOR NA STACK.
// SE O OPERADOR NO TOPO TIVER PRECEDENCIA MAIOR OU IGUAL,
// REMOVE O ANTERIOR, JOGA-O NA SAIDA E TENTA NOVAMENTE.
void PUSH(STACK& operators, const Operator& current_operator, BUFFER& POSFIX){
    if (current_operator.symbol == '(' || operators.empty()) {
        operators.push(current_operator);
        return;
    }

    Operator prev_operator = operators.top();
    if (prev_operator.precedence < current_operator.precedence ||
       prev_operator.symbol == '('){
        operators.push(current_operator);
        return;
    }
    
    operators.pop();
    POSFIX << prev_operator.symbol;
    PUSH(operators, current_operator, POSFIX);
}


// VERIFICA SE A FLAG DE PARENTESES ESTÁ LIGADA.
// CASO SIM REMOVE VALORES DA STACK ATÉ CHEGAR NO "(" E INSERE
// NA SAIDA, MENOS O "("
// DO CONTRÁRIO REMOVE ATÉ A STACK ACABAR.
void POP(STACK& operators, BUFFER& POSFIX, bool parentheses = true){
    while(!operators.empty()){
        Operator current_operator = operators.top();
        operators.pop();
        
        if (parentheses && current_operator.symbol == '(')
            return;

        POSFIX << current_operator.symbol;
    }
}


int main() {
    BUFFER OUTPUT; 

    int test_cases;
    cin >> test_cases;

    // ITERA SOBRE CADA CARACTER DA EXPRESSÃO INFIXA.
    // OPERANDOS SÃO ADICIONADOS NA EXPRESSÃO POSFIXA.
    // OPERADORES SÃO ADICIONADOS NA PILHA.
    for(size_t i = 0; i < test_cases; i++){
        BUFFER POSFIX;
        STACK operators;
        string expression;
        cin >> expression;

        for(char chr : expression){
            switch (chr){
                case ')': { POP(operators, POSFIX);            break; }
                case '(': { PUSH(operators, {'(', 0}, POSFIX); break; }
                case '*': { PUSH(operators, {'*', 2}, POSFIX); break; }
                case '+': { PUSH(operators, {'+', 1}, POSFIX); break; }
                case '-': { PUSH(operators, {'-', 1}, POSFIX); break; }
                case '/': { PUSH(operators, {'/', 2}, POSFIX); break; }
                case '^': { PUSH(operators, {'^', 3}, POSFIX); break; }
                default: { POSFIX << chr;                     break; }
            }
        }

        POP(operators, POSFIX, false);

        OUTPUT << POSFIX.str() << "\n";
    }
    
    cout << OUTPUT.str(); 
    return 0;
}