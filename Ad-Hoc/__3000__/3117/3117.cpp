#include <iostream>
using namespace std;

int main() {
    
    int n_students, minimum_required;
    cin >> n_students >> minimum_required;
    
    int students_presents = 0;
    for(size_t i = 0; i < n_students; i++){
        int time_;
        cin >> time_;
        if(time_ <= 0) students_presents++;
    }
    
    cout << (
        students_presents >= minimum_required ? 
        "YES\n" : "NO\n");
    
    return 0;
}