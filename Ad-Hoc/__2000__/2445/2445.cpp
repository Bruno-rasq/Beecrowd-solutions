#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int total = 0;
    vector<int> segments(n, 0);
    for(size_t i = 0; i < n; i++){
        cin >> segments[i];
        total += segments[i];
    }
    
    sort(segments.begin(), segments.end());
    
    int ans = 0;
    for(size_t i = n - 1; i > 1; --i){
        total -= segments[i];
        if(segments[i] < total){
            ans =  i + 1;
            break;
        }
    }
    
    cout << ans << "\n";
}