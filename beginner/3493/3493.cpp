#include <iostream>

int main(){
    int currentRecord, attempt;

    while(std::cin >> currentRecord >> attempt){
        std::cout << ((currentRecord < attempt) ? "ok\n" : "no\n");
    }
}