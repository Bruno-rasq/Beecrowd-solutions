#include <iostream>

using namespace std;

int main() {
	
	int value;
	cin >> value;

	int ages = value / 365;
	value %= 365;

	int months = value / 30;
	value %= 30;

	int days = value;

	cout << ages << " ano(s)\n";
	cout << months << " mes(es)\n";
	cout << days << " dia(s)\n";
	
	return 0;
}