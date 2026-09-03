#include <iostream>
#include <limits>

using namespace std;

int hamming_distance(string str1, string str2){
    int distance = 0;
    for(int i = 0; i < str1.size(); i++){
        if(str1[i] != str2[i]) distance++;
    }
    return distance;
}

int main(){

    string str1;
    int k;
    cin >> str1 >> k;

    int indice = -1;
    float menor_distance = numeric_limits<float>::infinity();

    for(int i = 0; i < 5; i++){
        string str2;
        cin >> str2;

        int distance = hamming_distance(str1, str2);
        if(distance < menor_distance){
            menor_distance = distance;
            indice = i + 1;
        }
    }

    cout << indice << endl;
    cout << (menor_distance <= k ? menor_distance : -1) << endl;

    return 0;
}