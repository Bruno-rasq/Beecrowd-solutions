#include <iostream>
#include <tuple>
#include <limits>
#include <iomanip>

int main() {
    double infinito = std::numeric_limits<double>::infinity();

    std::tuple<double, double, int> table[5] = {
        {0.0,       400.00,         15},
        {400.01,    800.00,         12},
        {800.01,    1200.00,        10},
        {1200.01,   2000.00,        7},
        {2000.01,   infinito,       4},
    };

    double salary;
    std::cin >> salary;

    for (const std::tuple<double, double, int>& line : table) {
        double min = std::get<0>(line);
        double max = std::get<1>(line);
        int percent = std::get<2>(line);

        if (salary >= min && salary <= max) {
            double readjustment = (salary * percent) / 100.0;
            double newSalary = salary + readjustment;

            std::cout << std::fixed << std::setprecision(2);
            std::cout << "Novo salario: " << newSalary << std::endl;
            std::cout << "Reajuste ganho: " << readjustment << std::endl;
            std::cout << "Em percentual: " << percent << " %" << std::endl;
            break;
        }
    }

    return 0;
}