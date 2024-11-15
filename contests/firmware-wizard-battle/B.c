#include <stdio.h>

int main(){

    int mr_monica_age, children1, children2, children3, eldest;

    scanf("%d", &mr_monica_age);
    scanf("%d", &children1);
    scanf("%d", &children2);

    children3 = mr_monica_age - (children1 + children2);

    eldest = children1;
    if(children2 > eldest){
        eldest = children2;
    }
    if(children3 > eldest){
        eldest = children3;
    }

    printf("%d\n", eldest);
    
    return 0;
}