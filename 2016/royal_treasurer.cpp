/*
 * Author: Aadil Ahamed
 * royal_treasurer.cpp: Topcoder SRM 433 easy
 */

#include<iostream>
#include<cassert>
#include<vector>
#include<utility>

using namespace std;

class RoyalTreasurer
{
    public:
        int minimalArrangement(vector<int> A, vector<int> B)
        {
            int idx_a = 0, idx_b = 0;
            N = A.size();
            taken = vector<bool>( N );
            for( int i = 0; i < N; i++ )
            {
                idx_a = next_min( A );
                idx_b = next_max( B );
                swap( A[idx_a], A[idx_b] );
                taken[idx_b] = true;
            }
            return s_function( A, B ); 
        }

        int sum( vector<int>& A )
        {
            int sum = 0;
            for(int i = 0; i < A.size(); i++)
            {
                sum += A[i];
            }
            return sum;
        }

        int s_function( vector<int>& A, vector<int>& B)
        {
            int res = 0;
            for( int i = 0; i < A.size(); i++ )
            {
                res += A[i]*B[i];
            }
            return res;
        }

        int init_idx()
        {
            int idx_min = 0;
            while( taken[idx_min] )
            {
                idx_min++;
            }
            return idx_min;
        }

        int next_min( vector<int> A )
        {
            int idx_min = init_idx();
            int min = A[idx_min];
            for( int i = idx_min; i < A.size(); i++ )
            {
                if( A[i] <= min && !taken[i] )
                {
                    min = A[i];
                    idx_min = i;
                }
            }
            return idx_min;
        }

        int next_max( vector<int> B )
        {
            int idx_max = init_idx();
            int max = B[idx_max];
            for( int i = idx_max; i < B.size(); i++ )
            {
                if( B[i] >= max && !taken[i] )
                {
                    max = B[i];
                    idx_max = i;
                }
            }
            return idx_max;
        }
        
        // Data Members
        vector<bool> taken;
        int N;
};

void test_sum()
{
    cout << "---- Test sum ----" << endl;
    vector<int> A;
    int res, exp;
    RoyalTreasurer rt;
    A = {1,1,13};
    res = rt.sum( A );
    exp = 15;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    A = {0,1,2,3,4,5};
    res = rt.sum( A );
    exp = 15;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
}

void test_init_idx()
{
    cout << "---- Test init_idx ----" << endl;
    vector<bool> taken; 
    int res, exp;
    RoyalTreasurer rt;
    rt.taken = {true, true, false, true, false};
    res = rt.init_idx();
    exp = 2;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    rt.taken = {false, true, false, true, false};
    res = rt.init_idx();
    exp = 0;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    rt.taken = {true, true, true, true, false};
    res = rt.init_idx();
    exp = 4;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp ); 
}

void test_next_min()
{
    cout << "---- Test next_min ----" << endl;
    RoyalTreasurer rt;
    int res, exp;
    vector<int> A;
    A = {1, 2, 0, 5, 3};
    rt.taken = {true, false, true, false, false};
    res = rt.next_min( A );
    exp = 1;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp ); 
    A = {1, 2, 0, 5, 3};
    rt.taken = {true, true, true, false, false};
    res = rt.next_min( A );
    exp = 4;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp ); 
    A = {1, 2, 0, 5, 3};
    rt.taken = {true, true, true, false, true};
    res = rt.next_min( A );
    exp = 3;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp ); 
}

void test_min_arr()
{
    cout << "---- Test min_arrange ----" << endl;
    RoyalTreasurer rt;
    vector<int> A {1,1,3};
    vector<int> B {10,30,20};
    int res = rt.minimalArrangement( A, B );
    int exp = 80;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    A = {1,1,1,6,0};
    B = {2,7,8,3,1};
    res = rt.minimalArrangement( A, B );
    exp = 18;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    A = {5,15,100,31,39,0,0,3,26};
    B = {11,12,13,2,3,4,5,9,1};
    res = rt.minimalArrangement( A, B );
    exp = 528;
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
}

void test()
{
    test_sum();
    test_init_idx();
    test_next_min();
    test_min_arr();
}

int main()
{
    test();
    return 0;
}
