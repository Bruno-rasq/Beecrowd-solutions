#include <iostream>
#include <cmath>

using namespace std;

int main(){
	
	int value;
	cin >> value;

	int hours = floor(value / 3600);
	int minutes = floor((value - (hours * 3600)) / 60);
	int secunds = value % 60;

	cout << hours << ":" << minutes << ":" << secunds << endl;
	
	return 0;
}