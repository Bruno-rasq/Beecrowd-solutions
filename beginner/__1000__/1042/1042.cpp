#include <iostream>
#include <vector>

using namespace std;

vector<int> simpleSort(vector<int> values){
    int len = values.size();
    for(int i = 0; i < len; i++){
        for(int j = 0; j < len - i - 1; j++){
            if(values[i] > values[j + 1]){
                int temp = values[j];
                values[j] = values[j + 1];
                values[j + 1] = temp;
            }
        }
    }
    return values;
}

int main(){
     int a, b, c;
     cin >> a >> b >> c;

     vector<int> values = {a, b, c};
     vector<int> sorted = simpleSort(values);

     for(int value : sorted){
        cout << value << endl;
     }

     cout << "" << endl;
     cout << a << endl;
     cout << b << endl;
     cout << c << endl;

    return 0;
}