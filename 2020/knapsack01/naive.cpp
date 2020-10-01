#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int helper(
    const vector<int> &weights,
    const vector<int> &profits,
    int capacity,
    int i ) {

    // cout << " i: " << i << " c: " << capacity << endl;
    
    if( i >= weights.size() ) {
        // base case
        return 0;
    }

    int p0 = 0, p1 = 0;
    int newCapacity = capacity - weights[ i ];
    if( newCapacity >= 0 ) {
        // select i
        p0 = profits[ i ] + helper( weights, profits, newCapacity, i+1 );
    }
    // don't select i
    p1 = helper( weights, profits, capacity, i+1 ); 
    return max( p0, p1 );
}

int
knapsack( 
    const vector<int> &weights,
    const vector<int> &profits,
    int capacity ) {
    return helper( weights, profits, capacity, 0 );
}
