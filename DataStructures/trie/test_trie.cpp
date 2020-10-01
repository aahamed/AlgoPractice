#include <iostream>
#include <string>
#include "assert.h"
#include "trie.h"

using namespace std;
using namespace MyTrie;

void
testInsertAndSearch() {
   cout << "Testing insert and search" << endl;
   string w1 = "cat";
   string w2 = "dog";
   Trie t;
   t.insert( w1 );
   assert( t.search( w1 ) );
   assert( !t.search( w2 ) );
}

int 
main() {
    cout << "Testing Trie" << endl;
    testInsertAndSearch();
    return 0;
}
