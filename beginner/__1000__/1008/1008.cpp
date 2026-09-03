#include <iostream>
#include <iomanip>

using namespace std;

int main() {

	int employee_number, worked_hours;
	double received_per_hour, salary;

	cin >> employee_number >> worked_hours >> received_per_hour;

	salary = received_per_hour * worked_hours;

	cout << "NUMBER = " << employee_number << endl;
	cout << "SALARY = U$ " << fixed << setprecision(2) << salary << endl;

	return 0;
}