#include <bits/stdc++.h>
using namespace std;

const int TARGETSTATE = 1023; // 1023 -> 1111111111 -> todos leds on.

/*
    CRIANDO MÁSCARAS DE BITS:

    Botão -> LEDs afetados       Máscara (LED10 ... LED1)  Decimal

    1  -> 2, 5                   0000010010                18
    2  -> 1, 3, 5, 6             0000110101                53
    3  -> 2, 4, 6, 7             0001101010                106
    4  -> 3, 7                   0001000100                68
    5  -> 1, 2, 6, 8             0010100011                163
    6  -> 2, 3, 5, 7, 8, 9       0111010110                470
    7  -> 3, 4, 6, 9             0100101100                300
    8  -> 5, 6, 9, 10            1100110000                816
    9  -> 6, 7, 8, 10            1011100000                736
    10 -> 8, 9                   0110000000                384
*/
const int MASK[11] = {0, 18, 53, 106, 68, 163, 470, 300, 816, 736, 384};

// LIGA: led mudando estado do bit de 0 para 1
void ON(int& state, int led){ state |= (1 << (led - 1)); }

// DESLIGA: led mudando estado do bit de 1 para 0
void OFF(int& state, int led){ state &= ~(1 << (led - 1)); }

// TOGGLE: inverte o estado do led 
void TOGGLE(int& state, int led) { state ^= (1 << (led - 1));}

// aplica a mascara referente ao botão pressionado.
void APPLYMASK(int& state, int button) { state ^= MASK[button]; }

// armazena o estado atual e os botões presionados para chegar no mesmo.
struct StateNode { int state; vector<int> buttons; };

StateNode BFS(int state) {
    queue<StateNode> states;
    bool visited[1024] = {};
    states.push({state, {}});
    visited[state] = true;
    while (!states.empty()) {
        StateNode curr = states.front();
        states.pop();
        if (curr.state == TARGETSTATE) return curr;
        for (int i = 1; i <= 10; i++) {
            StateNode next = curr;
            APPLYMASK(next.state, i);
            if (!visited[next.state]) {
                visited[next.state] = true;
                next.buttons.push_back(i);
                states.push(next);
            }
        }
    }
    return {state, {}}; // sem solução
}

int main() {
    int state = 0;
    for (int i = 1; i <= 10; i++) {
        int led;
        cin >> led;
        if (led) ON(state, i);
    }

    if(state == TARGETSTATE){
        cout << "0\n";
        return 0;
    }

    StateNode ans = BFS(state);

    if (ans.buttons.empty()) {
        cout << "-1\n";
        return 0;
    }

    cout << ans.buttons.size() << "\n";
    cout << ans.buttons[0];
    for (size_t i = 1; i < ans.buttons.size(); i++)
        cout << " " << ans.buttons[i];
    cout << "\n";

    return 0;
}