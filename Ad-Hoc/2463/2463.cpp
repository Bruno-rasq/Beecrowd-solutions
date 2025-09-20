#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(){

    int n;
    cin >> n;

    vector<int> arr(n);
    for(size_t i = 0; i < n; i++){
        cin >> arr[i];
    }

    int local_max = arr[0];
    int global_max = arr[0];

    for(size_t i = 1; i < n; i++){
        local_max = max(arr[i], local_max + arr[i]);
        if(local_max > global_max){
            global_max = local_max;
        }
    }

     cout << global_max << endl;
     return 0;
}