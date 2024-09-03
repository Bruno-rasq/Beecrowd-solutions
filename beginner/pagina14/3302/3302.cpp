#include <cstdio>

using namespace std;

int main() {
	int casos;
	scanf("%d", &casos);

	for(int i = 0; i < casos; i++)
	{
		int curr;
		scanf("%d", &curr);

		printf("resposta %d: %d\n", (i + 1), curr);
	}
	
	return 0;
}