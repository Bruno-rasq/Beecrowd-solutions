#include <iostream>
#include <queue>
#include <map>
#include <string>
using namespace std;

void printNameList(map<int, queue<string>>& list, int& n){
    string out = "";
    for(auto& [key, names]: list){
        if(names.empty()) continue;
        if(out.size() > 0) out += ", ";
        string name = names.front();
        names.pop();
        out += name;
        n--;
    }
    cout << out << "\n";
}

int main(){
    int n;
    cin >> n;
    map<int, queue<string>> list;
    for(size_t i = 0; i < n; i++){
        string name;
        cin >> name;
        list[name.size()].push(name);
    }
    while(n > 0){
        printNameList(list, n);
    }
}