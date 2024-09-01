#include <iostream>
#include <iomanip>

using namespace std;

double sphere(double raio) {
	const double PI = 3.14159;
	return (4.0/3.0) * PI * (raio * raio * raio);
}

int main() {
	double raio;
	cin >> raio;
	cout << "VOLUME = " << fixed << setprecision(3) << sphere(raio) << endl; 
	return 0;
}