#include <iostream>
#include <map>
#include <string>
#include <iomanip>
#include <limits>

using namespace std;

typedef map<string, int> Freq_t;
typedef map<float, Freq_t> RelativeFreq_t;

/* Lê todas as linhas e concatena */
string readText(int n){
    string text;
    string line;
    for(int i = 0; i < n; i++){
        getline(cin, line);
        text += line;
    }
    return text;
}

/* Conta digrafos */
void registerDigrafoFrequence(Freq_t& freq, int& totalDigrafos, const string& text){
    for(size_t pos = 0; pos + 1 < text.size(); pos++){
        string digrafo = "";
        digrafo += text[pos];
        digrafo += text[pos + 1];
        freq[digrafo]++;
        totalDigrafos++;
    }
}

/* Calcula frequência relativa */
RelativeFreq_t calcRelativeafrec(Freq_t& freq, int T){
    RelativeFreq_t RF;
    for(auto [digrafo, frequence] : freq){
        float relativeFreq = (float)frequence / T;
        RF[relativeFreq][digrafo] = frequence;
    }
    return RF;
}

/* Mostra top 5 */
void top5(const RelativeFreq_t& RF){
    int printed = 0;
    for(auto it = RF.rbegin(); it != RF.rend(); ++it){
        float relative_freq = it->first;
        for(const auto& [digraph, absolute_freq] : it->second){
            cout << digraph
                 << " "
                 << absolute_freq
                 << " "
                 << fixed << setprecision(6)
                 << relative_freq
                 << '\n';
            printed++;
            if(printed == 5) return;
        }
    }
}

int main(){
    int n;
    while(cin >> n && n != 0){
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        string text = readText(n);
        Freq_t digrafosFreq;
        int totalDigrafos = 0;
        registerDigrafoFrequence( digrafosFreq, totalDigrafos, text);
        RelativeFreq_t RF = calcRelativeafrec(digrafosFreq, totalDigrafos);
        top5(RF);
        cout << '\n';
    }
}