#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <functional>
using namespace std;

const int LIMIT = 100000;

vector<function<int(int,int)>> MATHF = {
    [](int a, int b){ return a + b; }, // SUM
    [](int a, int b){ return a - b; }, // SUB
    [](int a, int b){ return a * b; }, // MUL
    [](int a, int b){                  // DIV
        if (b != 0 && a % b == 0)
            return a / b;
        return 0;
    }
};

struct State {
    int value;
    int operations;
};

int BFS(int source, int target, const vector<int>& nums){
    if (source == target) return 0;
    queue<State> q;
    unordered_set<int> vis;
    q.push({source, 0});
    vis.insert(source);

    while(!q.empty()){
        State curr = q.front();
        q.pop();
        if(curr.value == target) return curr.operations;
        for(int n : nums){
            for(auto& f : MATHF){
                int nextValue = f(curr.value, n);
                if(nextValue >= 1 && nextValue <= LIMIT && !vis.count(nextValue)){
                    vis.insert(nextValue);
                    q.push({nextValue, curr.operations + 1});
                }
            }
        }
    }
    return -1;
}

int main(){
    int source, target, n;
    cin >> source >> target >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++)
        cin >> nums[i];

    cout << BFS(source, target, nums) << "\n";
}