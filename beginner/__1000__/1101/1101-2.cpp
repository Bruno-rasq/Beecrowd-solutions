#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    while(cin >> n >> m && n > 0 && m > 0){
        stringstream buffer_ans;
        int left = min(n, m);
        buffer_ans << left;
        int sum = left;
        for(size_t i = left + 1; i <= max(n, m); i++){
            buffer_ans << " " << i;
            sum += i;
        }
        buffer_ans << " Sum=" << sum << "\n";
        cout << buffer_ans.str();
    }
    return 0;
}