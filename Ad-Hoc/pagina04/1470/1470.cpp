#include <bits/stdc++.h>
using namespace std;

struct Tape {
    vector<int> tape;

    bool operator==(const Tape& other) const {
        return tape == other.tape;
    }
};

struct TapeHash {
    size_t operator()(const Tape& t) const {
        size_t h = 0;
        for (int x : t.tape)
            h = h * 31 + hash<int>()(x);
        return h;
    }
};

vector<int> folding(const vector<int>& tape, int idx) {
    int n = tape.size();

    if (idx == 0) {
        vector<int> ans = tape;
        reverse(ans.begin(), ans.end());
        return ans;
    }

    if (idx == n)
        return tape;

    vector<int> next;

    int overlap = min(idx, n - idx);

    // parte da esquerda que não sofreu sobreposição
    for (int i = 0; i < idx - overlap; i++)
        next.push_back(tape[i]);

    // parte sobreposta
    for (int k = 0; k < overlap; k++) {
        int left  = tape[idx - overlap + k];
        int right = tape[idx + overlap - 1 - k];
        next.push_back(left + right);
    }

    return next;
}

bool BFSFolding(const Tape& source, const Tape& target) {
    queue<Tape> q;
    unordered_set<Tape, TapeHash> vis;

    q.push(source);
    vis.insert(source);

    while (!q.empty()) {
        Tape curr = q.front();
        q.pop();

        if (curr == target)
            return true;

        if (curr.tape.size() == 1)
            continue;

        for (int i = 0; i <= (int)curr.tape.size(); i++) {
            Tape next{ folding(curr.tape, i) };

            if (vis.find(next) == vis.end()) {
                vis.insert(next);
                q.push(next);
            }
        }
    }

    return false;
}

int main() {
    int n, m;

    while (cin >> n) {
        vector<int> sourceTape(n);
        for (int i = 0; i < n; i++)
            cin >> sourceTape[i];

        cin >> m;

        vector<int> targetTape(m);
        for (int i = 0; i < m; i++)
            cin >> targetTape[i];

        Tape source{sourceTape};
        Tape target{targetTape};

        bool ans = BFSFolding(source, target);

        cout << (ans ? "S" : "N") << '\n';
    }
}