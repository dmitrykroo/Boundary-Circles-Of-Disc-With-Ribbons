/**
 Author: Dmitry Protasov
 Task 1.5.3c
 Number of boundary components for a word length 2n
*/

#include <iostream>
#include <vector>
#include <set>
using namespace std;
#define rep(i, a, b) for(int i = a; i < b; ++i)

const int N = 5000;

int n, answer = 0, was[N];
vector <int> pos[N];
vector <int> g[N];
string s;
set <int> letters;

bool check_word_on_correct() {
    for (auto c : letters) {
        if (pos[c].size() != 2) {
            printf("The symbol '%c' does not occur twice.\n", c);
            return 0;
        }
    }
    return 1;
}

bool check_graph_on_correct() {
    rep(v, 0, 4 * n) {
        if (g[v].size() != 2) {
            puts("The graph is incorrect!");
            return 0;
        }
    }
    return 1;
}

void connect(int u, int v) {
    g[u].push_back(v);
    g[v].push_back(u);
}

void make_ribbons() {
    for (auto c : letters) {
        int x = pos[c][0], y = pos[c][1];
        if (x > y) swap(x, y);
        connect(2 * x, 2 * y + 1);
        connect(2 * x + 1, 2 * y);
    }
}

void go(int v) {
    if (was[v]) return;
    was[v] = 1;
    go(g[v][0]);
    go(g[v][1]);
}

void calc_answer() {
    answer = 0;
    fill(was, was + 4 * n, 0);
    rep(v, 0, 4 * n) {
        if (!was[v]) {
            answer++;
            go(v);
        }
    }
}

void clear_data() {
    rep(i, 0, 2 * n) {
        pos[s[i]].clear();
    }
    letters.clear();
    rep(i, 0, 4 * n) {
        g[i].clear();
    }
    fill(was, was + 4 * n, 0);
}

main() {
    while (1) {
        clear_data();
        cout << "\nEnter a word in lowercase Latin letters, such that each letter occurs in it exactly twice\n";
        cin >> s;
        n = s.size() / 2;
        rep(i, 0, 2 * n) {
            pos[s[i]].push_back(i);
            letters.insert(s[i]);
        }
        if (!check_word_on_correct()) continue;
        rep(v, 0, 2 * n) {
            connect(2 * v + 1, (2 * v + 2) % (4 * n));
        }
        make_ribbons();
        if (!check_graph_on_correct()) continue;
        calc_answer();
        cout << "The number of boundary components is " << answer << "\n";
        clear_data();
    }
}