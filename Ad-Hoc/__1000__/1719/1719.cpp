/*
    memory 32bytes
    pc     5bits
    accu   8bits

    comprimento de uma instrução de 8 bits em que os 3 bits mais 
    significativos representam o codigo da operação a ser executada,
    e os 5 bits menos significativos definem um endereço de memoria.

    operaçoes: 

    000xxxxx    STA x   store the value of the accu int memory byte x
    001xxxxx    LDA x   load the value of memory byte x into the accu
    010xxxxx    BEQ x   if the value of the accu is 0 load the value x into the pc
    011-----    NOP     no operation
    100-----    DEC     subtract 1 from the accu
    101-----    INC     add 1 into the accu
    110xxxxx    JMP x   load the value x into the pc
    111-----    HLT     termiante the program.
*/

#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

const int MEMORYSIZE = 32; // 32 bytes
bool loadingMemory(vector<uint8_t>& mem);
void runProgram(vector<uint8_t>& mem);

int main(){
    vector<uint8_t> MEMORY(MEMORYSIZE);
    while(loadingMemory(MEMORY)){
        runProgram(MEMORY);
    }
    return 0;
}

/** carrega os dados de input na memoria do programa. */
bool loadingMemory(vector<uint8_t>& mem){
    for(size_t i = 0 i < MEMORYSIZE; i++){
        string binaryInput;
        if(!(cin >> binaryInput)) return false; // EOF
        mem[i] = stoi(binaryInput, nullptr, 2);
    }
    return true;
}

void runProgram(vector<uint8_t>& mem){
    // reset da CPU
    uint8_t pc = 0; // program counter
    uint8_t accu = 0; // acumulador

    while(true){
        uint8_t instruction = mem[pc];
        pc = (pc + 1) % MEMORYSIZE; // incrementa ciclicamente o pc

        /* Desloca 5 bits para direita sobrando apenas os 3 bits 
           mais significativos, estes definem qual operação ser
           executada.*/
        int operationCode = instruction >> 5;

        /* Utiliza uma mascara (0b11111 ou 31) e compara AND bit
           a bit com a instrução resoltando nos 5 bits menso signi-
           ficativos que definem um endereço de memoria. */
        int address = istruction & 31;

        switch(operationCode) {
            case 0: mem[address] = accu; break;                 // STA
            case 1: accu = mem[address]; break;                 // LDA
            case 2: if(accu == 0) pc = address; break;          // BEQ
            case 3: break;                                      // NOP
            case 4: accu--; break;                              // DEC
            case 5: accu++; break;                              // INC
            case 6: pc = address; break;                        // JMP
            case 7: cout << bitset<8>(accu) << "\n"; return;    // HLT
        }
    }
};