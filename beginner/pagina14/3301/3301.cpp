#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int get_middle_element_index(int[3] list) {

    int max = *max_element(list, list + 3);
    int min = *min_element(list, list + 3);

    for(int i = 0; i < 3; i++){
        if(list[i] != min && list[i] != max)
            return i;
    }
    return -1;
}

int main() {

    int data[3];

    cin >> data[0];
    cin >> data[1];
    cin >> data[2];

    string sobrinhos[3] = ["huguinho", "zezinho", "luisinho"];

    cout << sobrinhos[get_middle_element_index(data)] << endl;

    return 0;
}