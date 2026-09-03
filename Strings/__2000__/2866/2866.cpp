#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        string text, result;

        cin >> text;

        for(int j = 0; j < text.size(); j++){
            if(toupper(text[j]) != text[j]){
                reult += text[j];
            }
        }

        reverse(result.begin(), result.end());

        cout << result << endl;
    }

    return 0;
}