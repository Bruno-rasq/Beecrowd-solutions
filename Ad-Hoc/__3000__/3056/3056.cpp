#include <iostream>

using namespace std;

int main(){
    int steps;
    cin >> steps;
    
    long long nodes = 2;
    for (int i = 0; i < steps; i++) 
        nodes += (nodes - 1);
        
    cout << nodes * nodes << endl;
}