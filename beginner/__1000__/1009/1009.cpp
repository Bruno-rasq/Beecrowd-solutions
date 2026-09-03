#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	string name;
	double salary, sales, bonus;

	cin >> name >> salary >> sales;
	
	bonus = (sales * 15)/ 100;

	salary += bonus;

	cout << "TOTAL = R$ " << fixed << setprecision(2) << salary << endl;

	return 0;
}