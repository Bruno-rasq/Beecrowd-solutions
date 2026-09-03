#include <iostream>
#include <iomanip>

using namespace std;

int main(){

	int tempo, velocidade;
	double fuel;
	
	cin >> tempo >> velocidade;

	fuel = (tempo * velocidade) / 12.0;

	cout << fixed << setprecision(3) << fuel << endl;

	return 0;
}