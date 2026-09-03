#include <iostream>

using namespace std;

int main(){

	int value;

	cin >> value;

	cout << value << endl;

	cout << (value / 100) << " nota(s) de R$ 100,00" << endl;
	value %= 100;

	cout << (value / 50) << " nota(s) de R$ 50,00" << endl;
	value %= 50;

	cout << (value / 20) << " nota(s) de R$ 20,00" << endl;
	value %= 20;

	cout << (value / 10) << " nota(s) de R$ 10,00" << endl;
	value %= 10;

	cout << (value / 5) << " nota(s) de R$ 5,00" << endl;
	value %= 5;

	cout << (value / 2) << " nota(s) de R$ 2,00" << endl;
	value %= 2;

	cout << (value / 1) << " nota(s) de R$ 1,00" << endl;
	value %= 1;

	return 0;
}