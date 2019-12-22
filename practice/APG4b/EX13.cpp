#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> vec(N);
    for (int i = 0; i < vec.size(); i++) {
        cin >> vec.at(i);
    }
    int ans = 0;
    for (int i = 0; i < vec.size(); i++) {
        ans += vec.at(i);
    }
    ans /= N;
    for (int i = 0; i < vec.size(); i++) {
        cout << abs(vec.at(i) - ans) << endl;
    }
}
