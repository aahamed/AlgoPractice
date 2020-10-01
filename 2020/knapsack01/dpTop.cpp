#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static vector<vector<int>>* dpTop;

int helper(
    const vector<int> &weights,
    const vector<int> &profits,
    int capacity,
    int i ) {
    
    if( i >= weights.size() || capacity <= 0 ) {
        // base case
        return 0;
    }
    if( (*dpTop)[ i ][ capacity - 1 ] != -1 ) {
        // answer known
        return (*dpTop)[ i ][ capacity - 1 ];
    }
    int p0 = 0, p1 = 0, maxProfit = 0;
    int newCapacity = capacity - weights[ i ];
    if( newCapacity >= 0 ) {
        p0 = profits[ i ] + helper( weights, profits, newCapacity, i+1 );
    }
    p1 = helper( weights, profits, capacity, i+1 );
    maxProfit = max( p0, p1 );
    (*dpTop)[ i ][ capacity-1 ] = maxProfit;
    return maxProfit;
}

int
knapsack( 
    const vector<int> &weights,
    const vector<int> &profits,
    int capacity ) {
    dpTop = new vector<vector<int>>( weights.size(), vector<int>( capacity, -1 ) );
    int maxProfit = helper( weights, profits, capacity, 0 );
    delete dpTop;
    return maxProfit;
}
