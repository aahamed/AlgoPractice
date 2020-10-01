#include <iostream>
#include <algorithm>

using namespace std;

void
computeSumStack( int N, int K, int plateStack[100][31], int sumStack[100][31] ) {
    for( int i = 0; i < N; ++i ) {
        for( int j = 1; j <= K; ++j ) {
            sumStack[i][j] = sumStack[i][j-1] + plateStack[i][j];
        }
    }
}

int
dpMaxBeauty( int N, int K, int P, int stackId, int plateStack[100][31], int sumStack[100][31], int dp[100][1500] ) {
    if( stackId >= N ) {
        return 0;
    }
    // check if this subproblem is already solved
    if( dp[stackId][P] ) {
        //cout << "P: " << P << " stackId: " << stackId << " dp[stackId][P]: " << dp[stackId][P] << endl;
        return dp[stackId][P];
    }
    int maxBeauty = 0;
    for( int i = 0; i <= K && i <= P; ++i ) {
        int beauty = dpMaxBeauty( N, K, P-i, stackId+1, plateStack, sumStack, dp )
            + sumStack[stackId][i];
        if( beauty > maxBeauty ) {
            maxBeauty = beauty;
        }
    }
    //cout << "P: " << P << " stackId: " << stackId << " maxBeauty: " << maxBeauty << endl;
    dp[stackId][P] = maxBeauty;
    return maxBeauty;
}

int
naiveMaxBeauty( int N, int K, int P, int stackId, int plateStack[100][31], int sumStack[100][31] ) {
    if( stackId >= N ) {
        return 0;
    }
    int maxBeauty = 0;
    for( int i = 0; i <= K && i <= P; ++i ) {
        int beauty = naiveMaxBeauty( N, K, P-i, stackId+1, plateStack, sumStack )
            + sumStack[stackId][i];
        if( beauty > maxBeauty ) {
            maxBeauty = beauty;
        }
    }
    // cout << "P: " << P << " stackId: " << stackId << " maxBeauty: " << maxBeauty << endl;
    return maxBeauty;
}

int main() {
    int T, N, K, P;
    cin >> T;
    for( int i = 1; i <= T; ++i ) {
        cin >> N >> K >> P;
        int plateStack[100][31] = {0};
        int sumStack[100][31] = {0};
        int dp[100][1500] = {0};
        for( int j = 0; j < N; ++j ) {
            for( int k =1; k <= K; ++k ) {
                cin >> plateStack[j][k]; 
            }
        }
        computeSumStack( N, K, plateStack, sumStack );
        int maxBeauty = dpMaxBeauty( N, K, P, 0, plateStack, sumStack, dp );
        cout << "Case #" << i << ": " << maxBeauty << endl;
    }
    return 0;
}
