#include <iostream>
#include <string>
#include <sstream>
#include <vector>

bool isValidPet(const std::string& especie, const std::string& raca, const std::string& nome) {
    if (especie != "cachorro") return false;

    std::istringstream iss(nome);
    std::string palavra;
    std::vector<std::string> partes;

    while (iss >> palavra) {
        partes.push_back(palavra);
    }

    if (partes.size() < 2) return false; // precisa ser nome composto

    char inicialRaca = tolower(raca[0]);
    for (const auto& parte : partes) {
        if (tolower(parte[0]) == inicialRaca) {
            return true;
        }
    }

    return false;
}

int main() {
    int n;
    while (std::cin >> n) {
        std::cin.ignore(); // ignorar newline após o número
        int validos = 0;

        for (int i = 0; i < n; ++i) {
            std::string especie, raca, nome;

            std::getline(std::cin, especie);
            std::getline(std::cin, raca);
            std::getline(std::cin, nome);
            std::string linhaVazia;
            std::getline(std::cin, linhaVazia); // ler linha vazia

            if (isValidPet(especie, raca, nome)) {
                ++validos;
            }
        }

        std::cout << validos << std::endl;
    }

    return 0;
}