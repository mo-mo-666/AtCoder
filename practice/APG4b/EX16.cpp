#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> data(5);
    for (int i = 0; i < 5; i++)
    {
        cin >> data.at(i);
    }

    int before = -1;
    int after = -2;
    for (int x : data) {
        after = x;
        if (before == after) {
            cout << "YES" << endl;
            return 0;
        }
        before = x;
    }
    cout << "NO" << endl;
    // dataの中で隣り合う等しい要素が存在するなら"YES"を出力し、そうでなければ"NO"を出力する
    // ここにプログラムを追記
}
