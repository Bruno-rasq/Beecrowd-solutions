#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	double a, b, average;
	cin >> a >> b;

	average = (3.5 * a + 7.5 * b) / 11.0;

	cout << "MEDIA = " << fixed << setprecision(5) << average << 
 endl;
	return 0;
}