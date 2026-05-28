#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> primes;

void sieve(){
    vector<bool> isPrime(1000001, true);
    isPrime[0] = isPrime[1] = false;
    for(int i = 2; i <= 1000000; i++){
        if(isPrime[i]){
            primes.push_back(i);
            if(1LL * i * i <= 1000000){
                for(int j = i * i; j <= 1000000; j += i)
                    isPrime[j] = false;
            }
        }
    }
}

int mod(const string& K, int p){
    int r = 0;
    for(char c : K){
        r = (r * 10 + (c - '0')) % p;
    }
    return r;
}

int main(){
    sieve();
    string K;
    int L;
    while((cin >> K >> L) && !(K == "0" && L == 0)){
        bool bad = false;
        for(int p : primes){
            if(p >= L) break;
            if(mod(K, p) == 0){
                cout << "BAD " << p << '\n';
                bad = true;
                break;
            }
        }
        if(!bad) cout << "GOOD\n";
    }
}