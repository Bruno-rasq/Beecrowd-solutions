#include <iostream>
#include <vector>
using namespace std;

// OBJETIVO DO PROBLEMA É PEGAR O MENOR NODE DE CADA NIVEL EM 
// UMA ÁRVORE BINÁRIA DE BUSCA. UMA ÁRVORE BINÁRIA É SEPARA SEUS
// NODES EM LADO ESQUERDO (MENOR QUE O NODE ATUAL) E LADO
// DIREITO (MAIOR QUE O NODE ATUAL).

struct Node {
    int value;
    Node* left;
    Node* right;

    Node(int data){
        value = data;
        left = nullptr;
        right = nullptr;
    }
};

// LER OS INPUTS E CRIAR A ÁRVORE.
Node* INSERT(Node*& root, int value){
    if(root == nullptr){
        root = new Node(value);
        return root;
    }

    if(value < root->value)
        return INSERT(root->left, value);
    else
        return INSERT(root->right, value);

    return root;
}

// FAZER UMA TRAVESSIA ENTRE OS NODES DA ÁRVORE.
// TRAVESSIA PRE ORDER PASSA PELA RAIZ -> LEFT -> RIGHT
void PREORDER(Node* root, vector<bool>& nvls, int nvl){
    if(root == nullptr) return;
    
    if(nvls[nvl] == false){
        cout << nvl << " " << root->value << "\n";
        nvls[nvl] = true;
    }

    PREORDER(root->left, nvls, nvl + 1);
    PREORDER(root->right, nvls, nvl + 1);
}


int main() {

    Node* root = nullptr;     // RAIZ DA ÁRVORE.
    int n;                    // NUMERO DE NODES NA ÁRVORE.
    cin >> n;

    for(size_t i = 0; i < n; i++){
        int value;
        cin >> value;
        INSERT(root, value);
    }

    vector<bool> nivels(n, false);
    PREORDER(root, nivels, 0);

    return 0;
}