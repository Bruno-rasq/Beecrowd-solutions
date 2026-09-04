#include <iostream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <cmath> // fabs para comparação com double

using namespace std;

class CppTemplatesAndSTLContainers {
public:
    static void findIndicesWithSum(const vector<double>& array, double target) {
        bool has_value = false;
        const double EPS = 1e-9; // tolerância para comparação de double

        for (size_t i = 0; i < array.size(); i++) {
            for (size_t j = i + 1; j < array.size(); j++) {
                if (fabs(array[i] + array[j] - target) < EPS) {
                    cout << i << " " << j << " "
                              << fixed << setprecision(0) << target << "\n";
                    has_value = true;
                }
            }
        }
        if (!has_value) {cout << "null value\n";}
    }
};

int main() {
    vector<double> arr;
    double target, value;
    string line;

    // lê a linha inteira de números
    getline(cin, line);
    // lê o target em seguida
    cin >> target;

    // transforma a linha em números
    stringstream ss(line);
    while (ss >> value) {
        arr.push_back(value);
    }
    
    CppTemplatesAndSTLContainers::findIndicesWithSum(arr, target);
    return 0;
}