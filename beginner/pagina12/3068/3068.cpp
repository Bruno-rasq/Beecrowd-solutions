#include <iostream>
using namespace std;

int main(){
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    int i = 1;
    while (x1 != 0 && y1 != 0 && x2 != 0 && y2 != 0){
        int n, meteoros = 0;
        cin >> n;

        for(int j = 0; j < n; j++){
            int x, y;
            cin >> x >> y;
            if (x1 <= x && x <= x2 && y2 <= y && y <= y1) {
                meteoros++;
            }
        }

        cout << "Teste " + to_string(i) << endl;
        cout << meteoros << endl;

        i++;
        cin >> x1 >> y1 >> x2 >> y2;
    }
    return 0;
}