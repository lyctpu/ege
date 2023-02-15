#include <iostream>
#include <cmath>

using namespace std;

bool check_odd_divisors(int n) {
    int odd_divisors = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            if (i % 2 != 0) {
                odd_divisors++;
            }
            if (i != n / i && n / i % 2 != 0) {
                odd_divisors++;
            }
        }
    }
    return odd_divisors == 5;
}

int main() {

    for (int i = 35000000; i <= 40000000; i++) {
        if (check_odd_divisors(i)) {
            cout << i << endl;
        }
    }

    cout << "Все" << endl;
    return 0;
}
