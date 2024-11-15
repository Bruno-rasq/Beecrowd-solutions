#include <stdio.h>

int count_toothpicks(int p, int n, int c, int measurements[n][p]){
    int toothpick_count = 0;

    for(int j = 0; j < p; j++){
        int count = 0;

        for(int i = 0; i < n; i++){
            if(measurements[i][j] == 1){
                count++;
            } else {
                if(count >= 0){
                    toothpick_count++;
                }
                count = 0;
            }
        }

        if(count >= 0){
            toothpick_count++;
        }
    }

    return toothpick_count;
}

int main(){

    int p, n, c;

    while(1){
        scanf("%d %d %d", &p, &n, &c);
        if(p == 0 && n == 0 && c == 0){
            break;
        }

        int measurements[n][p];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < p; j++){
                scanf("%d", measurements[i][j]);
            }
        }

        int result = count_toothpicks(p, n, c, measurements);
        prinf("%d\n", result);
    }

    return 0;
}