#include <bits/stdc++.h>
using namespace std;

unordered_map<string, vector<string>> graph;

struct Node {
    string node;
    vector<string> nodes;
};

int BFS(string source, string target){
    queue<Node> q;
    unordered_set<string> vis;
    q.push({source, {}});
    vis.insert(source);
    while(!q.empty()){
        Node curr = q.front();
        q.pop();
        if(curr.node == target) return curr.nodes.size();
        for(string next: graph[curr.node]){
            if(vis.find(next) == vis.end()){
            	vector<string> nextnodes = curr.nodes;
            	nextnodes.push_back(next);
                vis.insert(next);
                q.push({next, nextnodes});
            }
        }
    }
    return -1;
}

int main() {
    int nodes, edges;
    string nodeA, nodeB;
    cin >> nodes >> edges;
    for(size_t i = 0; i < edges; i++){
        cin >> nodeA >> nodeB;
        graph[nodeA].push_back(nodeB);
        graph[nodeB].push_back(nodeA);
    }

    int ans = BFS("Entrada", "*") + BFS("*", "Saida");
    cout << ans << "\n";
}