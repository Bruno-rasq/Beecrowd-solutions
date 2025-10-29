#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int N;
    while (cin >> N) {
        vector<int> ages(N);
        for (int i = 0; i < N; ++i)
            cin >> ages[i];

        sort(ages.begin(), ages.end());

        int lethality = 0;
        int left = 0, right = N - 1;
        while (left < right) {
            lethality += abs(ages[right] - ages[left]);
            left++;
            right--;
        }

        cout << lethality << endl;
    }
}