#include <iostream>
#include <string>
using namespace std;

void removeAllSubsequences(string& seg_s, const string& seg_p) {
    int n = seg_s.size();
    int m = seg_p.size();
    int pos = -1;
    for (int i = 0; i <= n - m; i++) {
        if (seg_s.substr(i, m) == seg_p) {
            pos = i;
            break;
        }
    }
    if (pos != -1) {
        seg_s.erase(pos, m);
        removeAllSubsequences(seg_s, seg_p);
        return;
    }
    cout << (seg_s.empty() ? "null value" : seg_s) << '\n';
}

int main() {
    string segment_s, segment_p;
    cin >> segment_s >> segment_p;
    removeAllSubsequences(segment_s, segment_p);
}