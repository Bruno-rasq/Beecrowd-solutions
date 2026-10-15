#include <iostream>
#include <sstream>
using namespace std;

/*
    BROKEN KEYBOARD, A TECLA HOME E END SÃO PRESSIONADAS ALEATÓRIO
    QUANDO ISSO ACONTECE O CURSOR MUDA DE POSIÇÃO E CRIA UM TEXTO
    ERRADO.

    IDEIA USAR UM LISTA DUPLAMENTE ENCADEADA PARA INSERIR OS CARACTERES
    NO INICIO OU NO FIM DO TEXTO DE FORMA MAIS RÁPIDA.
*/

class Node {
    public:
        string value;
        Node* prev = nullptr;
        Node* next = nullptr;
    
        Node(string value): value(value) {}
};

class DoubleLinkedList {
    public:
        Node* head = nullptr;
        Node* tail = nullptr;

        DoubleLinkedList(){};

        void InsertEnd(string value){
            Node* newNode = new Node(value);

            if(this->head == nullptr){
                this->head = newNode;
                this->tail = newNode;
            } else {
                newNode->prev = this->tail;
                this->tail->next = newNode;
                this->tail = this->tail->next;
            }
        }
    
        void InsertHome(string value){
            Node* newNode = new Node(value);

            if(this->head == nullptr){
                this->head = newNode;
                this->tail = newNode;
            } else {
                newNode->next = this->head;
                this->head->prev = newNode;
                this->head = this->head->prev;
            }
        }
    
        string join(){
            stringstream buffer;

            Node* pointer = this->head;

            while(pointer){
                buffer << pointer->value;
                pointer = pointer->next;
            }

            return buffer.str();
        }
};

#define DLL DoubleLinkedList

void APPEND(string& current_segment, bool HomePress, DLL& dll){
    if(current_segment == "")
        return;

    if(!HomePress) 
        dll.InsertEnd(current_segment);
    else 
        dll.InsertHome(current_segment);

    current_segment = "";
}

int main() {
    string line;

    while(getline(cin, line)){

        DLL dll;
        string current_segment = "";
        bool HomePress = false;
        
        for(char chr : line){
            switch(chr){
                default: { 
                    current_segment += chr; 
                    break; 
                }

                case '[': {
                    APPEND(current_segment, HomePress, dll);
                    HomePress = true;
                    break;
                }

                case ']': {
                    APPEND(current_segment, HomePress, dll);
                    HomePress = false;
                    break;
                }
            }
        }

        APPEND(current_segment, HomePress, dll);

        cout << dll.join() << "\n";
    }

    return 0;
}