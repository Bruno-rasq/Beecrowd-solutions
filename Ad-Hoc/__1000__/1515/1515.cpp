#include <iostream>

using namespace std;

int main()
{
	
	int casos;
	cin >> casos;

	while(casos != 0)
	{
		int ano, duracao, menor = 0;
		string planeta, response;
		
		for (int i = 0; i < casos; i++)
		{
			cin >> planeta >> ano >> duracao;
			
			if(menor == 0){
				response = planeta;
				menor = ano - duracao;
				
			} else {
				if( (ano - duracao) < menor){
					response = planeta;
					menor = ano - duracao;
				}
			}
		}

		cout << response << endl;
		
		cin >> casos;
	}

	
	return 0;
}