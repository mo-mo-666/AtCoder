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


// 素因数分解 O(n^0.5)
map<int, int> prime_factor(int n) {
    map<int, int> res;
    while (n % 2 == 0) {
        res[2]++;
        n /= 2;
    }
    for (int i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            res[i]++;
            n /= i;
        }
    }
    if (n != 1) {
        res[n] = 1;
    }
    return res;
}





//################################################
//simple test

int test_msg(bool test, string funcname) {
    if (test) {
        cout << "OK: " << funcname << endl;
        return 0;
    } else {
        cout << "NG: " << funcname << endl;
        return 1;
    }
}

int test_summary(int n) {
    if (n == 0) {
        cout << "ALL OK." << endl;
        return 0;
    } else {
        cout << "FAILED " << n << " tests." << endl;
        return 1;
    }
}

bool test_is_prime() {
    bool test = is_prime(101) && !is_prime(57);
    return test_msg(test, "is_prime");
}

bool test_divisor() {
    vector<int> div1 = divisor(12);
    int ans1[] = {1, 2, 3, 4, 6, 12};
    if (div1.size() != sizeof(ans1) / sizeof(ans1[0])) {
        return test_msg(false, "divisor");
    }
    for (int i = 0; i < sizeof(ans1) / sizeof(ans1[0]); i++) {
        if (div1[i] != ans1[i]) {
            return test_msg(false, "divisor");
        }
    }

    vector<int> div2 = divisor(101);
    int ans2[] = {1, 101};
     if (div2.size() != sizeof(ans2) / sizeof(ans2[0])) {
        return test_msg(false, "divisor");
    }
    for (int i = 0; i < sizeof(ans2) / sizeof(ans2[0]); i++) {
        if (div2[i] != ans2[i]) {
            return test_msg(false, "divisor");
        }
    }
    return test_msg(true, "divisor");
}

bool test_prime_factor() {
    map<int, int> pf = prime_factor(180);
    map<int, int> ans;
    ans.emplace(2, 2);
    ans.emplace(3, 2);
    ans.emplace(5, 1);
    return test_msg(pf == ans, "prime_factor");
}


int main() {
    int n = test_is_prime()
          + test_divisor()
          + test_prime_factor();

    return test_summary(n);
}
