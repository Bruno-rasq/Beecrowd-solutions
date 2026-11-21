#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {

    const vector<int> productPricesInCents = {400, 450, 500, 200, 150};

    int productCode, quantity;
    cin >> productCode >> quantity;

    float totalPrice = (productPricesInCents[productCode - 1] * quantity) / 100.0;

    cout << "Total: R$ " << fixed << setprecision(2) << totalPrice << "\n";

    return 0;
}