#include <iostream>
#include <vector>
using namespace std;

struct Viewer {
    int init_time;    // A partir de qual momento começou a visualizar.
    int increment;    // de quanto em quanto tempo visualiza novamente.
};

// Executa uma busca binaria tentando achar um tempo T tal que o total
// de views seja maior ou igual a meta de views estipulada.
long long binary_search(const vector<Viewer>& viewers, long long target){
    
    long long LEFT = 0;
    long long RIGHT = 2LL * 1000000000000000000LL;    // Limite para o tempo.
    long long answer = -1;

    while (LEFT <= RIGHT){
        long long MID_TIME = LEFT + (RIGHT - LEFT) / 2;

        long long total_views = 0;
        for(const Viewer& viewer : viewers){
            if (MID_TIME < viewer.init_time) continue;
            // calcula quantas views o viewer teve até T tempo.
            long long views = (MID_TIME - viewer.init_time) / viewer.increment + 1;
            total_views += views;
            if (total_views >= target) break;
        }

        if(total_views >= target){
            answer = MID_TIME;
            RIGHT = MID_TIME - 1;
        }
        else{
            LEFT = MID_TIME + 1;
        }
    }

    return answer;
}

int main() {
    int n_viewers;
    long long target;
    cin >> n_viewers >> target;

    vector<Viewer> viewers;
    int init_time, increment;
    for(int i = 0; i < n_viewers; i++){
        cin >> init_time >> increment;
        viewers.push_back({init_time, increment});
    }

    cout << binary_search(viewers, target) << "\n";
    return 0;
}