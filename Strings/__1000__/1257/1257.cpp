#include <iostream>
#include <vector>
using namespace std;

int arrayhash(vector<string>& list){
    int hash = 0;
    for (int i = 0; i < list.size(); i++){
        string line = list[i];
        for(int j = 0; j < list.size(); j++){
            char ch = line[j];
            int pos_alf = ch - "A";
            hash += (pos_alf + i + j);
        }
    }
    return hash;
}

int main(){

    int cases;
    cin >> cases;

    for(int i = 0; i < cases; i++){
        int n;
        cin >> n;
        vector<string> lines;
        for(int j = 0; j < n; j++){
            string line;
            cin>> line;
            lines.pop_back(line);
        }

        int response = arrayhash(lines);
        cout << response << endl;
        
    }

    return 0;
}