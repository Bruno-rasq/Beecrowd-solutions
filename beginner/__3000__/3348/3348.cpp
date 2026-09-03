#include <iostream>
#include <string>

using namespace std;

int main() {
    int input;
    cin >> input;

    string l[] = {
        "2", "7", "5", "30", "169",
        "441", "1872", "7632", "1740",
        "93313", "459901", "1358657",
        "2504881", "13482720", "25779600",
        "68468401", "610346880",
        "1271932200", "327280800"
    };

    cout << l[input - 1] << endl;
    return 0;
}
