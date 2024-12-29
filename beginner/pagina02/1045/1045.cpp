#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using VETOR = vector<float>;

VETOR sort_vetor(VETOR& vetor){
    for(size_t i = 0; i < vetor.size(); i++){
        for(size_t j = 0; j < vetor.size() - i - 1; j++){
            if(vetor[j] > vetor[j + 1]){
                float temp = vetor[j + 1];
                vetor[j + 1] = vetor[j];
                vetor[j] = temp;
            }
        }
    }
    return vetor;
}

int main(){
    VETOR vetor;

    for(size_t i = 0; i < 3; i++){
        float data;
        cin >> data;
        vetor.push_back(data);
    }
    
    vetor = sort_vetor(vetor);

    float a = vetor[0];
    float b = vetor[1];
    float c = vetor[2];

    float a2 = a * a;
    float bc2 = (b * b) + ( c * c);

    vetor<string> responses;

    if(a >= (b + c)){
        responses.push_back("NAOO FORMA TRIANGULO");
    } else {
        if(a2 == bc2){ responses.push_back("TRIANGULO RETANGULO");}
        if(a2 >  bc2){ responses.push_back("TRIANGULO OBTUSANGULO");}
        if(a2 <  bc2){ responses.push_back("TRIANGULO ACUTANGULO");}
        if(a == b && b == c){ responses.push_back("TRIANGULO EQUILATERO");}
        if((a == b && b != c) || (b == c && c != a) || (a == c && a != b)){
            responses.push_back("TRIANGULO ISOSCELES");
        }
    }

    for(const auto& data: responses)
        cout << data << endl;

    return 0;
}