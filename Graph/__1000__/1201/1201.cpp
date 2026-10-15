#include <iostream>
#include <sstream>
using namespace std;

/*
    BST II: OBJETIVO CRIAR UMA ÁRVORE DE BUSCA BINÁRIA QUE ACEITE
    ALGUMAS OPERAÇÕES, INCLUINDO INSERÇÃO, BUSCA E REMOÇÃO DE UM NODE

    A BST TAMBÉM DEVE IMPLEMENTAR UMA TRAVESSIA INFIXA, PREFIXA E POSFIXA.
*/

struct Node {
    int value;
    Node* left = nullptr;
    Node* right = nullptr;

    Node(int value) : value(value) {}
};

Node* insert(Node* node, int value){
    if(node == nullptr){
        node = new Node(value);
        return node;
    }

    if(node->value > value)
        node->left = insert(node->left, value);

    if(node->value < value)
        node->right = insert(node->right, value);

    return node;
}

bool search(Node* root, int value){
    Node* current = root;

    while(current){
        if(current->value == value) return true;

        if(current->value > value)
            current = current->left;
        else
            current = current->right;
    }

    return false;
}

Node* remove(Node* node, int value){
    if(node == nullptr) return nullptr;

    if(node->value > value){
        node->left = remove(node->left, value);
    }
    else if(node->value < value){
        node->right = remove(node->right, value);
    }
    else {
        // NODE SEM FILHOS
        if(node->left == nullptr && node->right == nullptr){
            delete node;
            return nullptr;
        }

        // NODE COM APENAS FILHO DIREITO
        else if(node->left == nullptr){
            Node* temp = node->right;
            delete node;
            return temp;
        }

        // NODE COM APENAS FILHO ESQUERDO
        else if(node->right == nullptr){
            Node* temp = node->left;
            delete node;
            return temp;
        }

        // NODE COM DOIS FILHOS
        else {
            Node* maxNode = node->left;

            while(maxNode->right){
                maxNode = maxNode->right;
            }

            node->value = maxNode->value;
            node->left = remove(node->left, maxNode->value);
        }
    }

    return node;
}

void INFIX(Node* node, stringstream& buffer, bool& first){
    if(node == nullptr) return;

    INFIX(node->left, buffer, first);

    if(!first) buffer << " ";
    buffer << node->value;
    first = false;

    INFIX(node->right, buffer, first);
}

void PREFIX(Node* node, stringstream& buffer, bool& first){
    if(node == nullptr) return;

    if(!first) buffer << " ";
    buffer << node->value;
    first = false;

    PREFIX(node->left, buffer, first);
    PREFIX(node->right, buffer, first);
}

void POSFIX(Node* node, stringstream& buffer, bool& first){
    if(node == nullptr) return;

    POSFIX(node->left, buffer, first);
    POSFIX(node->right, buffer, first);

    if(!first) buffer << " ";
    buffer << node->value;
    first = false;
}

int main() {

    Node* root = nullptr;
    
    string input;

    while(getline(cin, input)){
        stringstream iss(input);
        string op;

        iss >> op;

        if(op == "INFIXA"){
            stringstream buffer;
            bool first = true;

            INFIX(root, buffer, first);

            cout << buffer.str() << "\n";
        }
        else if(op == "PREFIXA"){
            stringstream buffer;
            bool first = true;

            PREFIX(root, buffer, first);

            cout << buffer.str() << "\n";
        }
        else if(op == "POSFIXA"){
            stringstream buffer;
            bool first = true;

            POSFIX(root, buffer, first);

            cout << buffer.str() << "\n";
        }
        else if(op == "I"){
            int value;
            iss >> value;

            root = insert(root, value);
        }
        else if(op == "R"){
            int value;
            iss >> value;

            root = remove(root, value);
        }
        else if(op == "P"){
            int value;
            iss >> value;

            if(search(root, value)){
                cout << value << " existe\n";
            }
            else {
                cout << value << " nao existe\n";
            }
        }
    }

    return 0;
}