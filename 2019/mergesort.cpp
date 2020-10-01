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

void merge( vector<int> &left, vector<int> &right, vector<int> &out ) {
    int i, j, k;
    i = 0; j = 0; k = 0;
    while( i < left.size() && j < right.size() ) {
        if( left[ i ] <= right[ j ] ) {
            out[ k ] = left[ i ];
            ++i;
        } else {
            // right[ j ] < left[ i ]
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
}

void mergeSort( vector<int> &vIn ) {

    // base case
    if( vIn.size() <= 1 ) {
        return;
    }

    // recursive split
    auto mid = vIn.begin() + vIn.size() / 2;
    vector<int> left ( vIn.begin(), mid );
    vector<int> right ( mid, vIn.end() );
    mergeSort( left );
    mergeSort( right );
    merge( left, right, vIn );
}


int main() {
    cout << " MergeSort algorithm " << endl;
    int arrayIn[] = { 22, 14, 17, 8, 22, 9, 14, 3 };
    vector<int> v1 ( arrayIn, arrayIn + 8 );
    cout << " Input vector: ";
    printVector( v1 );
    mergeSort( v1 );
    cout << " sorted vector: ";
    printVector( v1 );
    return 0;
}
