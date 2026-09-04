#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N;
    cin >> N;
    
    vector<int> sections (N, 0);
    for(size_t i = 0; i < N; i++)
        cin >> sections[i];
        
    int idx_init = 0;
    int idx_end = N - 1;
    int side_a = sections[idx_init];
    int side_b = sections[idx_end];
    
    while(idx_init != idx_end){
        if(side_a < side_b) {
            idx_init++;
            side_a += sections[idx_init];
        }
        else {
            idx_end--;
            side_b += sections[idx_end];
        }
    }
    
    cout << idx_init + 1 << endl;
    return 0;
}