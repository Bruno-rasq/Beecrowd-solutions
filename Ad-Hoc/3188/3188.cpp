#include <iostream>
#include <vector>
using namespace std;

struct Node {
    vector<Node*> next;
    bool end = false;
    int digit;
};

bool insertNode(Node* root, string& phone){
    Node* curr = root;
    for(char digit : phone){
        if(curr->end) return false;  // número existente é prefixo

        Node* child = nullptr;
        for(Node* node : curr->next){
            if(node->digit == digit){
                child = node;
                break;
            }
        }

        if(child == nullptr){
            child = new Node;
            child->digit = digit;
            curr->next.push_back(child);
        }

        curr = child;
    }

    // número novo é prefixo de outro
    if(curr->end || !curr->next.empty()) return false;

    curr->end = true;
    return true;
}

int main() {
    int T;
    cin >> T;
    while(T--){
        Node* root = new Node;
        bool consistent = true;
        string cellphonenumber;
        int NCellPhone;
        cin >> NCellPhone;
    
        while(NCellPhone--){
            cin >> cellphonenumber;
            if(!consistent) continue;
            if(!insertNode(root, cellphonenumber))
                consistent = false;
        }
        
        cout << (consistent ? "YES\n" : "NO\n");
    }
}