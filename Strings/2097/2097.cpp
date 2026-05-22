#include <iostream>
#include <unordered_map>
#include <sstream>
using namespace std;

const unordered_map<string, long long> NAMENUMBERS = {
    {"zero", 0}, {"um", 1}, {"uma", 1}, {"dois", 2}, {"duas", 2},
    {"tres", 3}, {"quatro", 4}, {"cinco", 5}, {"seis", 6}, {"sete", 7},
    {"oito", 8}, {"nove", 9}, {"dez", 10}, {"onze", 11}, {"doze", 12},
    {"treze", 13}, {"quatorze", 14}, {"quinze", 15}, {"dezesseis", 16},
    {"dezessete", 17}, {"dezoito", 18}, {"dezenove", 19}, {"vinte", 20},
    {"trinta", 30}, {"quarenta", 40}, {"cinquenta", 50}, {"sessenta", 60},
    {"setenta", 70}, {"oitenta", 80}, {"noventa", 90}, {"cem", 100},
    {"cento", 100}, {"duzentos", 200}, {"trezentos", 300}, {"quatrocentos", 400},
    {"quinhentos", 500}, {"seiscentos", 600}, {"setecentos", 700},
    {"oitocentos", 800}, {"novecentos", 900}, {"mil", 1000}, {"milhao", 1000000LL},
    {"milhoes", 1000000LL}, {"bilhao", 1000000000LL}, {"bilhoes", 1000000000LL},
    {"trilhao", 1000000000000LL}, {"trilhoes", 1000000000000LL},
    {"quatrilhao", 1000000000000000LL}, {"quatrilhoes", 1000000000000000LL},
};

int main() {
    string number;
    while(getline(cin, number)){
        istringstream iss(number);
        string token;
        long long total = 0;
        long long group = 0;
        while (iss >> token) {
            // ignora conectores
            if (token == "e") continue;
            long long value = NAMENUMBERS.at(token);
            // escalas grandes
            if (value == 1000LL || value == 1000000LL || value == 1000000000LL ||
                value == 1000000000000LL) {
                // caso: "mil"
                // multiplicador implícito
                if (group == 0) group = 1;
                group *= value;
                // mil e acima fecham grupo
                total += group;
                group = 0;
                continue;
            }
            // centenas/dezenas/unidades
            group += value;
        }
        cout << total + group << "\n";
    }
}