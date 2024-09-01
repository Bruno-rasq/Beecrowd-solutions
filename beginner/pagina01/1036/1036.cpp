#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

void bhaskara(double a, double b, double delta) {
	double r1 = (-b + sqrt(delta)) / (2 * a);
	double r2 = (-b - sqrt(delta)) / (2 * a);

	cout << "R1 = " << fixed << setprecision(5) << r1 << endl;
	cout << "R2 = " << fixed << setprecision(5) << r2 << endl;
}

int main(){

	double a, b, c, delta;
	cin >> a >> b >> c;

	delta = pow(b, 2) - (4 * a * c);

	if (a != 0 && delta > -1){
		bhaskara(a, b, delta);
		
	} else {
		cout << "Impossivel calcular\n";
	}
	
	return 0;
}