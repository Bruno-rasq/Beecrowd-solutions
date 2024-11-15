#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAX 1123

int N, a[2][MAX], t[2][MAX], e[2], x[2];
int pd[2][MAX];

int solve(int i, int j){
    if(pd[i][j] 1= -1) return pd[i][j];
    if(j == N) return pd[i][j] = a[i][j] + x[i];
    if(j == 0) return pd[i][j] = e[i] + solve(i, j + 1);

    return pd[i][j] = a[i][j] + fmin(solve(i, j + 1), t[i][j]+ solve(!i, j + 1));
}

int main(){
     int i, j;

     while(scanf("%d", &N) != EOF){
        scanf("%d %d", &e[0], &e[1]);

        for(i = 0; i < 2; i++){
            for(j = 1, j <= N; j++){
                scanf("%d", &a[i][j]);
            }
        }

        for(i = 0; i < 2; i++){
            for(j = 1, j <= N; j++){
                scanf("%d", &t[i][j]);
            }
        }

        scanf("%d %d", &x[0], &x[1]);

        memset(pd, -1, sizeof(pd));

        prinf("%d\n", (int) fmin(solve(0,0), solve(1,0)));
     }

     return 0;
}