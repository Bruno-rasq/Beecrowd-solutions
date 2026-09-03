#include <stdio.h>

struct child_t {
    char name[30];
    int value;
    int prev, next;
};

int main()
{
    while (1) {
        int N, i, j;
        struct child_t child[100];

        scanf("%d", &N);
        if (!N)
            break;

        for (i = 0; i < N; ++i) {
            scanf("%s%d", child[i].name, &child[i].value);

            child[i].prev = ((i - 1) % N + N) % N;
            child[i].next = (i + 1) % N;
        }

        i = 0;
        while (N > 1) {
            int value = child[i].value;

            if (value % 2) {
                for (j = 0; j < value; ++j)
                    i = child[i].next;
            } else {
                for (j = 0; j < value; ++j)
                    i = child[i].prev;
            }

            child[child[i].prev].next = child[i].next;
            child[child[i].next].prev = child[i].prev;

            --N;
        }
        i = child[i].next;

        printf("Vencedor(a): %s\n", child[i].name);
    }

    return 0;
}