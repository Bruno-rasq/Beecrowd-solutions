#include <stdio.h>
#include <string.h>

void verificarPalavra(char *palavra, char *resultado){

    if(strlen(palavra) == 3){
        if(strncmp(palavra, "OB", 2) == 0){
            strcpy(resultado, "OBI");
        } 
        else if (strncmp(palavra, "UR", 2) == 0) {
            strcpy(resultado, "URI");
        }
        else {
            strcpy(resultado, palavra);
        }
    } else {
        strcpy(resultado, palavra);
    }
}

int main() {
    int n;

    scanf("%d", &n);

    char palavras[n][21];
    for (int i = 0; i < n; i++){
         scanf("%s", palavras[i]);
    }

    char resultado[21 * n];
    resultado[0] = '\0';

    char palavraCorrigida[21];
    for (int i = 0; i < n; i++){
        verificarPalavra(palavras[i], palavraCorrigida);
        strcat(resultado, palavraCorrigida);
        if(i < n - 1){
            strcat(resultado, " ");
        }
    }

    printf("%s\n", resultado);
    return 0;
}