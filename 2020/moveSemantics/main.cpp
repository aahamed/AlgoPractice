#include <iostream>
#include <vector>
#include "Move.h"

using namespace std;

void
printLen( Move m0 ) {
    cout << " printLen: " << m0._length << endl;
}

int
main() {
    cout << " Move Semantics " << endl;
    /*Move m0 { 10 };
    Move m1 { m0 };
    Move m2 { move( m0 ) };
    cout << " m2 len: " << m2._length << endl;
    printLen( m0 );
    printLen( Move{ 15 } );*/
    vector<Move> v;
    v.push_back( Move{ 25 } );
    v.push_back( Move{ 35 } );
    cout << " about to insert" << endl;
    v.insert( v.begin()+1, 95 );
    for( auto &iter : v ) {
        cout << " in loop len: " << iter._length << endl;
    }
    return 0;
}
