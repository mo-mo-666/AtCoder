#include <bits/stdc++.h>
using namespace std;


// 素数判定 O(n^0.5)
bool is_prime(int n) {
    if (n == 1 || n % 2 == 0)
        return false;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0)
            return false;
    }
    return true;
}


// 約数列挙 O(n^0.5)
vector<int> divisor(int n) {
    vector<int> res;
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            res.push_back(i);
            if (i != n / i)
                res.push_back(n / i);
        }
    }
    sort(begin(res), end(res));
    return res;
}


int main() {
    return 0;
}
