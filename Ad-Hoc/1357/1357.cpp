#include <iostream>
#include <tuple>
#include <string>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

typedef tuple<string, string, string> Braille;

const map<string, Braille> STR_TO_BRAILLE = {
    {"1", {"*.", "..", ".."}},  {"2", {"*.", "*.", ".."}}.
    {"3", {"**", "..", ".."}},  {"4", {"**", ".*", ".."}}.
    {"5", {"*.", ".*", ".."}},  {"6", {"**", "*.", ".."}}.
    {"7", {"**", "**", ".."}},  {"8", {"*.", "**", ".."}}.
    {"9", {".*", "*.", ".."}},  {"0", {".*", "**", ".."}}.
};

const map<string, Braille> BRAILLE_TO_STR = {
    {{"*.", "..", ".."}, "1"},  {{"*.", "*.", ".."}, "2"}.
    {{"**", "..", ".."}, "3"},  {{"**", ".*", ".."}, "4"}.
    {{"*.", ".*", ".."}, "5"},  {{"**", "*.", ".."}, "6"}.
    {{"**", "**", ".."}, "7"},  {{"*.", "**", ".."}, "8"}.
    {{".*", "*.", ".."}, "9"},  {{".*", "**", ".."}, "0"}.
};

void translate_integer_to_braille(const string& message){
    vector<Braille> braille;
    for(const char& digit : message){
        string s(1, digit);
        braille.push_back(STR_TO_BRAILLE(s));
    }
    for(size_t i = 0; i < 3; i++){
        for(size_t j = 0; j < braille.size(); j++){
            if(i == 0) cout << get<0>(braille[j]);
            if(i == 1) cout << get<1>(braille[j]);
            if(i == 2) cout << get<2>(braille[j]);
            if(j != braille.size() - 1) cout << " ";
        }
    }
    cout << endl;
};

void translate_braille_to_integer(vector<Braille>& message){
    for(size_t i = 0; i < message.size(); i++){
        cout << BRAILLE_TO_STR.at(message[i]);
    }
    cout << endl;
};

int main(){
    int n;
    while(cin >> n){

        if (n == 0) break;

        char type;
        cin >> type;
        cin.ignore();

        if(type == "B"){
            vector<string> line(3);
            for(int i = 0; i < 3; i++){
                getline(cin, line[i]);
            }

            vector<Braille> message;
            message.reserve(n);

            vector<istringstream> streams;
            for(int i = 0; i < 3; i++){
                streams.push_back(istringstream(line[i]));
            }

            for(int j = 0; j < n; j++){
                string a, b, c;
                streams[0] >> a;
                streams[1] >> b;
                streams[2] >> c;
                message.push_back(Braille(a,b, c));
            }

            translate_braille_to_integer(message);
            continue;
        }

        string message;
        cin >> message;

        translate_integer_to_braille(message);

    }
    return 0;
}