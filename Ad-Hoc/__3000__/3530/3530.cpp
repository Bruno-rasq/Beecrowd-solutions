#include <iostream>
using namespace std;

int main() {

    int n;
    cin >> n;

    int left, right;
    int s, e, p;

    cin >> s >> e >> p;

    left = e - p;
    right = left;

    for(int i = 0; i < n; i++) {

        if(i > 0)
            cin >> s >> e >> p;

        right = max(right, s) + p;

        if(right > e)
            right = e;
    }

    cout << right - left << "\n";

    return 0;
}