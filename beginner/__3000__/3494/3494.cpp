#include <iostream>
#include <string>
#include <algorithm>

int distanceBetweenChars(char a, char b){
    return (b - a + 26) % 26;
}

int main(){

    std::string s, t;
    std::cin >> s >> t;

    int cost = 0;
    for(size_t i = 0; i < s.size(); i++){
        int minCost = std::min(
            distanceBetweenChars(s[i], t[i]),
            distanceBetweenChars(t[i], s[i])
        );
        cost += minCost;
    }
    std::cout << cost << '\n';

    return 0;
}