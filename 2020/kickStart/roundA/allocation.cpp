#include <iostream>
#include <algorithm>

using namespace std;

int
maxH( int N, int* A, int B ) {
    int i = 0, m = 0;
    sort( A, A+N );
    for( int i = 0; i < N && B >= 0; ++i ) {
        B -= A[ i ];
        if( B >= 0 ) {
            m++;
        }
    }
    return m;
}

int
main() {
    int A[ 100000 ];
    int N = 0, B = 0, T = 0;
    cin >> T;
    for( int i = 1; i <= T; ++i ) {
        cin >> N >> B;
        for( int j = 0; j < N; ++j ) {
            cin >> A[ j ];
        }
        cout << "Case #" << i << ": " << maxH( N, A, B ) << endl;
    }
    return 0;
}
