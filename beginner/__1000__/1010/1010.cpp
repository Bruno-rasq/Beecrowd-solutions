#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	int code1, quantity1, code2, quantity2;
	double price1, price2, total;

	cin >> code1 >> quantity1 >> price1;
	cin >> code2 >> quantity2 >> price2;

	total = (price1 * quantity1) + (price2 * quantity2);

	cout << "VALOR A PAGAR: R$ " << fixed << setprecision(2) << total << endl;
	
	return 0;
}