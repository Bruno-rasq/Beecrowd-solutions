#include <stdio.h>

void toHEXADECIMAL(int decimal, char *result){
    int index = 0;

    if(decimal == 0){
        result[index++] = '0';
        result[index] = '\0';
        return;
    }

    while(decimal > 0){
        int res = decimal % 16;

        if(res < 10){
            result[index++] = res + '0';
        } else {
            result[index++] = (res - 10) + 'A';
        }

        decimal /= 16;
    }

    result[index] = '\0';

    for(int i = 0; i < index / 2; i++){
        char temp = result[i];
        result[i] = result[index - i - 1];
        result[index - i - 1] = temp;
    }
}

int main() {
    int decimal;
    char result[20];

    scanf("%d", &decimal);

    toHEXADECIMAL(decimal, result);

    printf("%s\n", result);

    return 0;
}