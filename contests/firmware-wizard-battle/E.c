#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int lista[n];
    for (int i = 0; i < n; i++){
        scanf("%d", &lista[i]);
    }

    int multiples_2 = 0;
    int multiples_3 = 0;
    int multiples_4 = 0;
    int multiples_5 = 0;

    for(int i = 0; i < n; i++){
        int num = lista[i];

        if(num % 2 == 0) { multiples_2++; }
        if(num % 3 == 0) { multiples_3++; }
        if(num % 4 == 0) { multiples_4++; }
        if(num % 5 == 0) { multiples_5++; }
    }

    printf("%d Multiplo(s) de 2\n", multiples_2);
    printf("%d Multiplo(s) de 3\n", multiples_3);
    printf("%d Multiplo(s) de 4\n", multiples_4);
    printf("%d Multiplo(s) de 5\n", multiples_5);

    return 0;
}