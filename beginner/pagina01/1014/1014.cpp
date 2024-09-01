#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	
	int kilometers;
	double fuel;

	cin >> kilometers >> fuel;
	cout << fixed << setprecision(3) << (kilometers / fuel) << " km/l\n";
	
	return 0;
}