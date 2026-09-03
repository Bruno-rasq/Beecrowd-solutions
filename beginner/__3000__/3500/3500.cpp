#include <iostream>
#include <algorithm>

int main() {
    std::string numberOriginal;
    std::cin >> numberOriginal;
    std::swap(numberOriginal[0],  numberOriginal[2]);
    std::cout << "Invertido = ";
    std::cout << numberOriginal << "\n";
    return 0;
}