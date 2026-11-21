#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    
    const unordered_map<int, string> months = {
        {1, "January"}, 
        {2, "February"}, 
        {3, "March"}, 
        {4, "April"}, 
        {5, "May"}, 
        {6, "June"}, 
        {7, "July"}, 
        {8, "August"}, 
        {9, "September"}, 
        {10, "October"}, 
        {11, "November"}, 
        {12, "December"}
    };

    int input;
    cin >> input;
    cout << months.at(input) << "\n";
    return 0;
}