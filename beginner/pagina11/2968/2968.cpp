#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main(){

    int voltas, placas;
    cin >> voltas >> placas;

    double total_placas = stataic_cast<double>(voltas * placas);
    vector<int> results;

    for(int i = 10; i <= 90; i += 10){
        int qnt_placas_por_porcentagem = static_cast<int>(ceil((total_placas * i) / 100.0));
        results.push_back(qnt_placas_por_porcentagem);
    }

    string output;
    for(const int& result: results){
        output += to_string(result) + " ";
    }

    if(!output.empty()){
        output.pop_back();
    }

    cout << output << endl;

    return 0;
}