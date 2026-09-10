#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
using namespace std;

// DESENVOLVER UMA SISTEMA DE SPAM, NO QUAL UM GRUPO DE PESSOAS
// AMIGOS OU NÃO COMPARTILHAM O SPAM E GANHAM "TITULOS" COM BASE NA
// QUANTIDADE DE AMIGOS PARA OS QUAIS CADA PESSOA ENVIOU O SPAM.

struct User {
    vector<int> friends_ids;
    string out;
};

#define GRAPH vector<User>
#define SET unordered_set<int>
#define QUEUE queue<int>


// BFS - DADO UMA PESSOA X, DEVE PROPAGAR O SPAM PARA TODOS SEUS AMIGOS
// E PARA OS AMIGOS DE AMIGOS. (CADA PESSOA RECEBE 1 VEZ).
// forwarded[i] GUARDA QUANTOS AMIGOS A PESSOA i ENVIOU O SPAM.
void BFS(int start, GRAPH& web, vector<int>& forwarded) {
    SET achieved;
    QUEUE Q;

    Q.push(start);
    achieved.insert(start);

    while(!Q.empty()) {
        int curr = Q.front();
        Q.pop();

        forwarded[curr - 1] = web[curr - 1].friends_ids.size();

        for(int next : web[curr - 1].friends_ids) {
            if(achieved.find(next) == achieved.end()) {
                achieved.insert(next);
                Q.push(next);
            }
        }
    }
}


int main() {
    int n;

    while((cin >> n) && n != 0) {

        GRAPH web;

        // LE OS DADOS DO GRAFO.
        for(int i = 0; i < n; i++) {
            int adj_id;
            User user = {{}, ""};

            while((cin >> adj_id) && adj_id != 0)
                user.friends_ids.push_back(adj_id);

            web.push_back(user);
        }

        // COMPARTILHA OS SPAMS.
        int start;

        while((cin >> start) && start != 0) {

            int A1, A2;
            string T1, T2, T3;

            cin >> A1 >> A2 >> T1 >> T2 >> T3;

            vector<int> forwarded(n, 0);

            BFS(start, web, forwarded);

            // DETERMINA O ATRIBUTO DE CADA PESSOA.
            for(int person = 0; person < n; person++) {

                int range = forwarded[person];

                if(range < A1)
                    web[person].out += T1 + " ";
                else if(range < A2)
                    web[person].out += T2 + " ";
                else
                    web[person].out += T3 + " ";
            }
        }

        // LE OS NOMES DAS PESSOAS.
        for(int i = 0; i < n; i++) {

            string user_name;
            cin >> user_name;

            cout << user_name << ": " << web[i].out << "\n";
        }
    }

    return 0;
}