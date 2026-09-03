#include <iostream>
#include <string>

using namespace std;

typedef long long ll;

// Quantas vezes o LED atual desliga (O -> X).
// Esse valor será a quantidade de trocas do próximo LED.
ll N_toggle(char led_state, ll steps) {
    if (led_state == 'X')
        return steps / 2;

    return (steps + 1) / 2;
}

// Estado final após 'steps' trocas.
char toggle_led_state(char led_state, ll steps) {
    ll on_off = (led_state == 'O') ? 1 : 0;
    ll state = (on_off + steps) % 2;
    return state == 0 ? 'X' : 'O';
}

void log_painel_state(const string& leds, ll steps) {
    string ans = "";
    for (size_t i = 0; i < leds.size(); i++) {
        char led = leds[i];

        // Estado final deste LED.
        ans += toggle_led_state(led, steps);

        // Quantas vezes ele desligou = trocas do próximo.
        steps = N_toggle(led, steps);
    }
    cout << ans << '\n';
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string leds;
        ll steps;
        cin >> leds >> steps;
        log_painel_state(leds, steps);
    }
    return 0;
}