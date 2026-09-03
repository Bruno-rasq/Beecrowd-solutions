#include <iostream>
#include <iomanip>

using namespace std;

double triangulo(double a, double c){
	return (a * c) / 2.0;
}

double circle(double c){
	const double PI = 3.14159;
	return (c * c) * PI;
}

double trapezio(double a, double b, double c){
	return ((a + b) * c) / 2.0;
}

double square(double b){
	return b * b;
}

double retangle(double a, double b){
	return a * b;
}

int main(){

	double a, b, c;
	cin >> a >> b >> c;

	cout << "TRIANGULO: " << fixed << setprecision(3) << triangulo(a, c) << endl;
	cout << "CIRCULO: " << fixed << setprecision(3) << circle(c) << endl;
	cout << "TRAPEZIO: " << fixed << setprecision(3) << trapezio(a, b, c) << endl;
	cout << "QUADRADO: " << fixed << setprecision(3) << square(b) << endl;
	cout << "RETANGULO: " << fixed << setprecision(3) << retangle(a, b) << endl;
	
	return 0;
}