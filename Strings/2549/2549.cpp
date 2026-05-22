#include <iostream>
#include <unordered_map>
#include <sstream>
using namespace std;

void register_student(unordered_map<string, int>& SD, string year){
    string student_name;
    getline(cin, student_name);
    istringstream iss(student_name);
    string word, acronym;
    while(iss >> word){
        acronym += word[0];
    }
    SD[acronym + year]++;
}

int main(){
    int n;
    string year;
    while(cin >> n >> year){
        cin.ignore(); // <-- apenas aqui
        unordered_map<string, int> system_data;
        for(int i = 0; i < n; i++)
            register_student(system_data, year);
        int ans = 0;
        for (const auto& [key, value] : system_data) {
            if(value >= 2)
                ans += (value - 1);
        }
        cout << ans << endl;
    }
    return 0;
}