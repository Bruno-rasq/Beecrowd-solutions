#include <iostream>
#include <string>

using namespace std;

bool include(const string[] meses, int size, const string& mes){
    for(size_t i = 0; i < size; i++){
        if(meses[i] == mes){
            return true;
        }
    }
    return false;
}

int main(){

    string meses_com_31_dias[7] = {"january", "march", "may", "july", "august", "october", "december"};
    string meses_com_30_dias[4] = {"april", "june", "september", "november"};
    string meses_com_28_dias[1] = {"february"};

    int casos, resultado = 0;
    cin >> casos;

    for(size_t i = 0; i < casos; i++){
        string mes;
        int velas;

        cin >> mes >> velas;

        if(include(meses_com_31_dias, 7, mes)){
            resultado += 31 * velas;
            continue;
        }
        if(include(meses_com_30_dias, 4, mes)){
            resultado += 30 * velas;
            continue;
        }
        if(include(meses_com_28_dias, 1, mes)){
            resultado += 28 * velas;
            continue;
        }
    }

    cout << resultado << endl;
    return 0;

}