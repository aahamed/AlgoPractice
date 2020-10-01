#include <iostream>
#include "dpTop.cpp"

using namespace std;

int
main() {
    cout << " Knapsack0/1 " << endl;
    vector<int> w { 1, 2, 3, 4, 2, 5 };
    vector<int> p { 1, 6, 10, 16, 9, 18};
    int c = 7;
    int maxProfit = knapsack( w, p, c );
    cout << " MaxProfit: " << maxProfit << endl;
    return 0;
}
