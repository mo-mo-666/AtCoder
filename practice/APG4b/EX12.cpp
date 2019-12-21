#include <bits/stdc++.h>
using namespace std;

int main()
{
    string S;
    cin >> S;

    int result = S.at(0);
    for (int i = 1; i < S.size(); i += 2) {
        int p = S.at(i+1);
        switch (S.at(i)) {
            case '+':
            result += p
            case '-':
            result -= p
        }
    }
}
