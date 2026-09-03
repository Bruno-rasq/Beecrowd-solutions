
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

/*
    todas os Nodes da Trie anteriores a um Node com autocomplete off
    devem ser ignorado. o resultado para cada palavra é a quantidade 
    de nodes com autocomplete off no processos.
    
    nodes com autocomplete off são:
        - nodes com mais de um node filho
        - nodes no final de cada palavra 
*/
struct Node {
    char chr;
    bool autocomplete = true; // true = não precisa digitar
    vector<Node*> next;
};

void insert(Node* root, vector<string>& words) {
    // -------- Insert word in wordlist ----------
    string word;
    cin >> word;
    words.push_back(word);

    // -------- Insert word in trie ----------
    Node* current = root;

    for (char c : word) {
        Node* child = nullptr;
        // procura filho existente
        for (Node* node : current->next) {
            if (node->chr == c) {
                child = node;
                break;
            }
        }
        // cria caso não exista
        if (child == nullptr) {
            child = new Node;
            child->chr = c;
            current->next.push_back(child);
            // se surgiu uma bifurcação,
            // este nó passa a exigir digitação
            if (current->next.size() > 1)
                current->autocomplete = false;
        }
        current = child;
    }
    // fim de palavra também exige digitação
    current->autocomplete = false;
}

int count_typing(Node* root, const string& word) {
    int count = 0;
    Node* current = root;
    for (char chr : word) {
        for (Node* node : current->next) {
            if (node->chr == chr) {
                if (!node->autocomplete)
                    count++;
                current = node;
                break;
            }
        }
    }
    return count;
}

int main() {
    int n;

    while (cin >> n) {
        Node* root = new Node{};
        vector<string> words;

        for (int i = 0; i < n; i++)
            insert(root, words);

        int count = 0;
        for (string& word : words)
            count += count_typing(root, word);

        cout << fixed << setprecision(2) << count / static_cast<double>(n) << "\n";
    }
}