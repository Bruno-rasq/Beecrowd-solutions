#include <iostream>

// ascii a - z -> 97 a 122

int main(){
    int index;
    while(std::cin >> index){
        char ans = 'a' + (index - 1);
        std::cout << ans << std::endl;
    }
}