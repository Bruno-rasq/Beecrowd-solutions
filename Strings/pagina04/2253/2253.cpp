#include <iostream>
#include <cctype>

using namespace std;

int main(){

	int n;
	bool maiuscula, minuscula, numero, errado;
	string str;

	while(getline(cin, str)){
		n = str.length();

		if(n < 6 || n > 32){
			cout << "Senha invalida." << endl;
			continue;
		}
		
		errado = false, maiuscula = false, minuscula = false, numero = false;
		for(char ch: str){
			if(isalpha(ch)){
				if(isupper(ch)) maiuscula = true;
				else minuscula = true;
				
			} else if(isdigit(ch)){
				numero = true;
			} else {
				errado = true;
				break;
			}
		}

		if(errado || !(maiuscula && minuscula && numero)){
			cout << "Senha invalida." << endl;
		} else {
			cout << "Senha valida." << endl;
		}
	}
	
	return 0;
}