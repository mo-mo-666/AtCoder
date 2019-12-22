#include <bits/stdc++.h>
using namespace std;

int main()
{
    string S;
    cin >> S;

    int result = 1;
    for (int i = 1; i < S.size(); i += 2) {
        switch (S.at(i)) {
            case '+':
            result += 1;
            break;
            case '-':
            result -= 1;
            break;
        }
    }
    cout << result <<endl;
}
