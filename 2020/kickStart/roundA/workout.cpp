#include <iostream>
#include <algorithm>

using namespace std;

int fitnessProgram[ 200000 ];
int difficulty[ 200000 ];

void
printDifficulty( int N, int k ) {
    cout << "k: " << k << " difficulty: ";
    for( int i = 0; i < N+k-1; ++i ) {
       cout << difficulty[ i ] << " "; 
    }
    cout << endl;
}

int
findMaxDifficultyPos( int N, int k ) {

    int maxPos = 0, maxDifficulty = 0;
    // find max difficulty
    for( int i = 0; i < N + k; ++i ) {
        if( difficulty[ i ] >= maxDifficulty ) {
            maxPos = i;
            maxDifficulty = difficulty[ i ];
        }
    }
    return maxPos;
}

int
solve() {
    int N, K, maxPos = 0, maxDifficulty = 0;
    int minDifficulty = 0;
    cin >> N >> K;
    memset( fitnessProgram, 0, sizeof( fitnessProgram ) );
    memset( difficulty, 0, sizeof( difficulty ) );
    // read in fitness program
    for( int i = 0; i < N; ++i ) {
        cin >> fitnessProgram[ i ];
    }
    // init difficulty
    for( int j = 0; j < N-1; ++j ) {
        difficulty[ j ] = fitnessProgram[ j+1 ] - fitnessProgram[ j ];
    }
    //cout << "initial: " << endl;
    //printDifficulty( N, 0 );
    for( int k = 0; k < K; ++k ) {
        maxPos = findMaxDifficultyPos( N, k );
        maxDifficulty = difficulty[ maxPos ];
        if( maxDifficulty == 1 ) {
            break;
        }
        // split maxDifficulty ( 2 steps )
        // 1. shift all elements of difficulty right of maxPos to the right by 1
        for(int i = N + k; i > maxPos; --i ) {
            difficulty[ i+1 ] = difficulty[ i ];
        }
        // 2. split the difficulty value at maxPos between maxPos and maxPos+1
        difficulty[ maxPos ] = maxDifficulty / 2;
        difficulty[ maxPos+1 ] = maxDifficulty - difficulty[ maxPos ];
    }
    maxPos = findMaxDifficultyPos( N, K );
    return difficulty[ maxPos ];
}

int
main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for( int i = 1; i <= T; ++i ) {
        int maxDifficulty = solve();
        cout << "Case #" << i << ": " << maxDifficulty << endl;
    }
    return 0;
}
