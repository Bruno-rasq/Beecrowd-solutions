#include <iostream>
#include <array>
using namespace std;

struct Key {
    int ID; // o número da tecla: 0, 1, 2, 3... 9
    double amountOfOil; // valor com 2 casas decimais
};

/* algoritmo que ordena as teclas de acordo vom seu valor de oleo. */
void bubbleSort(array<Key, 10>& arr) {
    for (int i = 0; i < arr.size() - 1; i++)
        for (int j = 0; j < arr.size() - i - 1; j++)
            if (arr[j].amountOfOil < arr[j + 1].amountOfOil)
                swap(arr[j], arr[j + 1]);
}

int main(){
    int testCase = 1;
    int sizePassword;
    
    while(cin >>sizePassword) {
        array<Key, 10> keys;
        for(size_t IDKey = 0; IDKey < 10; IDKey++){
            double amountOil;
            cin >> amountOil;
            keys[IDKey] = {IDKey, amountOil};
        }
        bubbleSort(keys);
        string password = "";
        for(size_t i = 0; i < sizePassword; i++)
            password += to_string(keys[i].ID);
            
        cout << "Caso " << to_string(testCase) << ": " << password << "\n";
        testCase++;
    }
    return 0;
}