#include <string>

using namespace std;

namespace MyTrie {

#define SIZE 26

class Trie;

class Node {

friend class Trie;

public:
    ~Node();
    void insert( char c );
    Node * get( char c );

private:
    Node * children[ SIZE ];
    bool isWord;
};

class Trie {

public:
    Trie();
    ~Trie();
    void insert( string word );
    bool search( string word );

private:
    Node * root;
};

}
