#include <iostream>
#include <unordered_map>
#include <iomanip>

using namespace std;

int main() {

	int pedido, quantidade;
	unordered_map<int, double> cardapio;

	//preparando o cardapio.
	cardapio[1] = 4.00;
	cardapio[2] = 4.50;
	cardapio[3] = 5.00;
	cardapio[4] = 2.00;
	cardapio[5] = 1.50;

	//recebo os valores de entrada.
	cin >> pedido >> quantidade;

	double total = cardapio[pedido] * quantidade;

	cout << "Total: R$ " << fixed << setprecision(2) << total << endl;
	
	return 0;
}