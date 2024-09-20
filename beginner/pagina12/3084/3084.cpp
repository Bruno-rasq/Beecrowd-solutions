#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    int ah, am;

    while(cen >> ah >> am){
        
        int hh = ah / 30;
        int mm = am / 6;

        cout << setfill("0") << setw(2) << hh << setfil("0") << setw(2) >> mm << endl;
    }
    return 0;
}