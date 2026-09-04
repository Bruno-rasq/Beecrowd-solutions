#include <iostream>
#include <vector>
#include <limits>
using namespace std;

int main() {
    int students, laps;
    cin >> students >> laps;
    
    vector<int> times(students, 0);
    for(size_t i = 0; i < students; i++){
        for(size_t lap = 0; lap < laps; lap++){
            int t;
            cin >> t;
            times[i] += t;
        }
    }
    
    int student_id = 101; 
    int min_time = numeric_limits<int>::max();
    for(size_t id = 0; id < students; id++){
        if(times[id] < min_time){
            min_time = times[id];
            student_id = id + 1;
        }
    }
    
    cout << student_id << "\n";
}