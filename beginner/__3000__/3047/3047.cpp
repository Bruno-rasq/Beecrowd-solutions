#include <iostream>
using namespace std;

int main(){
    
    int mr_monica_ages, children_1, children_2;
    cin >> mr_monica_ages >> children_1 >> children_2;

    int children_3 = mr_monica_ages - (children_1 + children_2);

    int eldest = children_1;

    if(children_2 > eldest){ eldest = children_2 }
    if(children_3 > eldest){ eldest = children_3 }

    cout << eldest << endl;

    return 0;
}