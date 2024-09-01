#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	double a, b, c, average;
	cin >> a >> b >> c;

	average = (2 * a + 3 * b + 5 * c) / 10.0;

	cout << "MEDIA = " << fixed << setprecision(1) << average << 
 endl;
	return 0;
}