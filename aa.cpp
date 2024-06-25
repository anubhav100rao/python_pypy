#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "local/debug.cpp"
#else
#define debug(...) 42
#endif

#define dbg(x) cerr<<#x<<" = "<<x<<endl
#define int long long


signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    #ifndef ONLINE_JUDGE 
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        freopen("error.txt", "w", stderr);
    #endif

    vector<vector<int>> data = {
        {1, 0},
        {0, 1},
        {1, 0},
        {1, 0},
        {0, 1}
    };

    int count_males = 0, count_females = 0;
    int males_survivor = 0, females_survivor = 0;

    for(auto &row : data) {
        if(row[1] == 1) {
            count_males++;
            if(row[0] == 1) males_survivor++;
        } else {
            count_females++;
            if(row[0] == 1) females_survivor++;
        }
    }


    cout << "male survivor percentage:" << (males_survivor + 0.0) / (count_males) << "\n";
    cout << "females survivor percentage: " << (females_survivor + 0.0) / (count_females) << "\n";

    return 0;
}
