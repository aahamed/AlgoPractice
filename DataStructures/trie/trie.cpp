#include <iostream>
#include "trie.h"

#define offset( c ) c - 97

using namespace std;

namespace MyTrie {

Node::~Node() {
    for( int i = 0; i < SIZE; ++i ) {
        if( children[ i ] ) {
            delete children[ i ];
        }
    }
}

void
Node::insert( char c ) {
    cout << "Node::insert " << c << endl;
    children[ offset( c ) ] = new Node();
}

Node *
Node::get( char c ) {
    cout << "Node::get " << c << endl;
    return children[ offset( c ) ];
}

Trie::Trie() {
    root = new Node();
}

Trie::~Trie(){
    delete root;
}

void
Trie::insert( string word ) {
    cout << "Trie::insert " << word << endl;
    Node * curr = root;
    for( char& c : word ) {
        Node * next = curr->get( c );
        if( next ) {
            curr = next;
        } else {
            curr->insert( c );
            curr = curr->get( c );
        }
    }
    curr->isWord = true;
}

bool
Trie::search( string word ) {
    Node * curr = root;
    for( char& c : word ) {
        curr = curr->get( c );
        if( !curr ) {
            return false;
        }
    }
    return curr->isWord;
}

}
