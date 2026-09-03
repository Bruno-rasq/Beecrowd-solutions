#include <iostream>
#include <vector>

using namespace std;

int main(){

	int maior = 0;
	vector<int> vetor(3);

	cin >> vetor[0];
	cin >> vetor[1];
	cin >> vetor[2];

	for(int i = 0; i < 3; i++){
		if(maior < vetor[i])
			maior = vetor[i];
	}

	cout << maior << " eh o maior\n";
	
	return 0;
}