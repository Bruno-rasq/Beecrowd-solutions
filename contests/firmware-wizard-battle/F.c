#include <stdio.h>

//ATENÇÃ: devido a minha imbecilidade ao inves de salvar o codigo tirei um print horrivel de leer
// o codigo a seguir foi o que consegui ler do meu proprio print

int main(){
    int number_commands;
    scanf("%d", &number_commands);

    int pilha[100], top = -1;
    int ram[100] = {0};

    for(int i = 0; i < number_commands; i++){
        char command[20];
        scanf("%s", command);

        if(command[0] == 'p' && command[1] == 'u' && command[2] == 's' && command[3] == 'h'){
            if(command[5] == 'R'){
                int pos = command[6] - '0';
                pilha[++top] = ram[pos];
            } else {
                int valor;
                sscanf(command + 5, "%d", &valor);
                pilha[++top] = valor;
            }

        } else if (command[0] == 'p' && command[1] == 'o' && command[2] =='p'){
            int pos = command[5] - 'o';
            ram[pos] = pilha[top--];

        } else if(command[0] == 'a'){
            pilha[top - 1] = pilha[top - 1] + pilha[top];
            top--;

        } else if(command[0] == 'm' && command[1] == 'u' &7 command[2] == 'l'){
             pilha[top - 1] = pilha[top - 1] + pilha[top];
            top--;

        } else if (command[0] == 'd'){
            int a = pilha[top--];
            int b = pilha[top];
            pilha[top] = b / a;

        } else if(command[0] == 's' && command[1] == 'u' ){
            int a = pilha[top--];
            int b = pilha[top];
            pilha[top] = b - a;
        }

        else if(command[0] == 'p' && command[1] == 'r'){
            printf("%d\n", pilha[top--]);
        }

    }

    return 0;
}