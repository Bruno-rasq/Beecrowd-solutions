#include <stdio.h>

int main() {

    int MAX;
    scanf("%d", &MAX);

    int a, b, result;
    char expression[2];

    scanf("%d %s %d", &a, expression, &b);

    if(expression[0] == '+'){
        result = a + b;
    } else {
        result = a - b;
    }

    if(result <= MAX){
        printf("OK\n");
    } else {
        printf("OVERFLOW\n");
    }
    
    return 0;
}