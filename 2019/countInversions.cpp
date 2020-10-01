#include <iostream>
#include <vector>

using namespace std;


void
printVector( const vector<int> &v ) {
    for( auto i = v.cbegin(); i != v.end(); ++i ) {
        cout << " " << *i;
    }
    cout << endl;
}

int 
mergeAndCount( vector<int> &left, vector<int> &right, vector<int> &out ) {
    int i, j, k, splitCount;
    i = 0; j = 0; k = 0; splitCount = 0;
    while( i < left.size() && j < right.size() ) {
        if( left[ i ] <= right[ j ] ) {
            out[ k ] = left[ i ];
            ++i;
        } else {
            // right[ j ] < left[ i ]
            // this means split inversion
            splitCount += left.size() - i;
            out[ k ] = right[ j ];
            ++j;
        }
        ++k;
    }
    // copy remaining elements from left
    for( ; i < left.size(); ++i ) {
        out[ k ] = left[ i ];
        ++k;
    }
    // copy remaining elements from right
    for( ; j < right.size(); ++j ) {
        out[ k ] = right[ j ];
        ++k;
    }
    return splitCount;
}

int 
sortAndCount( vector<int> &vIn ) {

    // base case
    if( vIn.size() <= 1 ) {
        return 0;
    }

    // variables to keep track of left, right and split inversion count
    int leftCount, rightCount, splitCount;
    leftCount = 0; rightCount = 0; splitCount = 0;

    // recursive split
    auto mid = vIn.begin() + vIn.size() / 2;
    vector<int> left ( vIn.begin(), mid );
    vector<int> right ( mid, vIn.end() );
    leftCount = sortAndCount( left );
    cout << " left ( sorted ): ";
    printVector( left );
    cout << " left numInversions: " << leftCount << endl;
    rightCount = sortAndCount( right );
    cout << " right ( sorted ): ";
    printVector( right );
    cout << " right numInversions: " << rightCount << endl;
    splitCount = mergeAndCount( left, right, vIn );
    cout << " merged vector: ";
    printVector( vIn );
    cout << " split numInversions: " << splitCount << endl;
    return leftCount + rightCount + splitCount;
}


int main() {
    cout << " CountInversions algorithm " << endl;
    //int arrayIn[] = { 22, 14, 17, 8, 21, 9, 19, 3 };
    int arrayIn[] = { 5, 4, 3, 2, 1 };
    vector<int> v1 ( arrayIn, arrayIn + 5 );
    int numInversions = 0;
    cout << " Input vector: ";
    printVector( v1 );
    numInversions = sortAndCount( v1 );
    cout << " sorted vector: ";
    printVector( v1 );
    cout << " numInversions: " << numInversions << endl;
    return 0;
}
