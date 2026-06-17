
#include <iostream>
#include <numeric>
using namespace std;

bool tripla_pitagorica(int x, int y, int z){
    return (x*x + y*y) == z*z;
}

int mdc3(int a, int b, int c){
    return gcd(gcd(a, b), c);
}

int main(){
    int a, b, c;
    while(cin >> a >> b >> c){
        
        bool cond1 = tripla_pitagorica(a, b, c);
        bool cond2 = tripla_pitagorica(a, c, b);
        bool cond3 = tripla_pitagorica(b, c, a);
        string ans = "tripla";
        
        if(cond1 || cond2 || cond3){
            if(mdc3(a, b, c) == 1) 
                ans = "tripla pitagorica primitiva";
            else 
                ans = "tripla pitagorica";
        }
        
        cout << ans << "\n";
    }
}