#include <iostream>
#include <vector>
using namespace std;

void getRocks(vector<int>& rocks, int N) {
    rocks.clear();
    for (int i = 0; i < N; i++) {
        int curr;
        cin >> curr;
        rocks.push_back(curr);
    }
}

bool isSorted(const vector<int>& rocks) {
    for (size_t i = 1; i < rocks.size(); i++) {
        if (rocks[i - 1] > rocks[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int N;
    while (cin >> N, N != 0) {
        int count = 0; 
        vector<int> tentativa;

        while (true) {
            getRocks(tentativa, N);
            count++;

            if (isSorted(tentativa)) {
                cout << count << endl;
                break;
            }
        }
    }
    return 0;
}