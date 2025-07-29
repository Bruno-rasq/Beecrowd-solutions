#include <iostream>
using namespace std;

class BinaryHexadecimalNumberSystem {
public:
    static bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
};

int main() {
    
    int n;
    cin >> n;
    
    bool isPot = BinaryHexadecimalNumberSystem::isPowerOfTwo(n);
    cout << (isPot == 1 ? "true" : "false") << endl;
    
    return 0;
}