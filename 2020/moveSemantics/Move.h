#pragma once
#include <iostream>
#include <algorithm>

using namespace std;

class Move {

public:
    Move( int length ) : 
        _length( length ),
        _data( new int [ length ] ) {
        cout << " len: " << _length;
        cout << " constructor Move::Move(int)" << endl; 
    }

    ~Move() {
        cout << " len: " << _length;
        cout << " destructor Move::~Move()" << endl;
        delete[] _data;
    }

    Move( const Move& other ) :
        _length( other._length ),
        _data( new int [ other._length ] ) {
        cout << " len: " << _length;
        cout << " copy constructor Move::Move( const Move& )" << endl;
        copy(other._data, other._data + _length, _data);
    }

    Move& operator=( const Move& other ) {
        delete[] _data;
        _length = other._length;
        _data = new int[ _length ];
        std::copy(other._data, other._data + _length, _data);
        return *this;
    }

    Move( Move&& other ) :
        _length( 0 ),
        _data( nullptr ) {
        _length = other._length;
        _data = other._data;
        other._length = 0;
        other._data = nullptr;

        cout << " len: " << _length;
        cout << " move constructor Move::Move( const Move&& )" << endl;
    }

    Move& operator=( Move&& other ) {
        cout << " move assignment" << endl;
        delete[] _data;

        _length = other._length;
        _data = other._data;

        other._length = 0;
        other._data = nullptr;

        return *this;
    }


    int _length;
    int* _data;
};
