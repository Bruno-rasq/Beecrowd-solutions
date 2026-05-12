#include <iostream>

int main() {
    int messInTheWeek;
    std::cin >> messInTheWeek;
    std::string ans = "vai ficar sem o biscoito\n";
    if(messInTheWeek <= 3)
        ans = "vai ganhar o biscoito\n";
        
    std::cout << ans;
    return 0;
}