#include <iostream>
#include <vector>

using namespace std;

int main(){
	
	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++){

		int len, count = 0;
		vector<int> vet;

		cin >> len;
		for(int n= 0; n < len; n++){ //capturando dados do vetor
			int value;
			cin >> value;
			vet.push_back(value);
		}

		//implementando o algoritmo de bubble sort.
		for(int j =0; j < len - 1; j++){
			for(int k=0; k < len - j - 1; k++){
				if(vet[k] > vet[k + 1]){
					count++;
					int temp = vet[k];
					vet[k] = vet[k + 1];
					vet[k + 1] = temp;
				}
			}
		}

		cout << "Optimal train swapping takes " << count << " swaps." << endl;
		
	}
	
	return 0;
}