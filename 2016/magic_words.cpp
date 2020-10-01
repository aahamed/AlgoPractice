/*
 * Author: Aadil Ahamed
 * magic_words.cpp: srm 433
 */

#include<iostream>
#include<vector>
#include<string>
#include<cassert>
#include<utility>

using namespace std;

class MagicWords
{
    public:
        int count(vector<string> S, int K)
        {
            numMagicWords = 0;
            this->K = K;
            worker( S.size(), S );
            return numMagicWords;
        }

        void worker( int n, vector<string> A )
        {
            if( n == 1)
            {
                if( isMagicWord( createWord( A ), K ) )
                {
                    // cout << "magic word: " << createWord( A ) << endl;
                    numMagicWords++;
                }
            }
            else
            {
                int i = 0;
                while( true )
                {
                    worker( n-1, A );
                    if( i == (n-1) )
                    {
                        break;
                    }
                    if( n % 2 == 0 )
                    {
                        swap( A[i], A[n-1] );
                    }
                    else
                    {
                        swap( A[0], A[n-1] );
                    }
                    i++;
                }
            }
        }

        string createWord( vector<string> S )
        {
            string word;
            for( string& w : S )
            {
                word += w;
            }
            return word;
        }

        bool isMagicWord( string word, int K )
        {
            int L = word.size();
            int numSame = 0;
            for( int i = 0; i < L; i++ )
            {
                bool same = true;
                for(int j = 0; j < L; j++)
                {
                    if( word[j] != word[(i+j)%L] )
                    {
                        same = false;
                        break;
                    }
                }
                if( same )
                {
                    // cout << "cycle i = " << i << " is same" << endl; 
                    numSame++;
                }
            }
            if( numSame == K )
            {
                return true;
            }
            return false;
        }

        void generate( vector<string> A )
        {
            generate( A.size(), A);
        }

        void generate( int n, vector<string> A )
        {
            if( n == 1)
            {
                printVector( A );
            }
            else
            {
                int i = 0;
                while( true )
                {
                    generate( n-1, A );
                    if( i == (n-1) )
                    {
                        break;
                    }
                    if( n % 2 == 0 )
                    {
                        swap( A[i], A[n-1] );
                    }
                    else
                    {
                        swap( A[0], A[n-1] );
                    }
                    i++;
                }
            }
        }

        void printVector( vector<string> A )
        {
            cout << "[ ";
            for( string& word : A )
            {
                cout << word << " ";
            }
            cout << "]" << endl;
        }

        int numMagicWords = 0;
        int K = 0;
};

void test_generate()
{
    cout << "---- Test generate ----" << endl;
    MagicWords mw;
    vector<string> S;
    S = {"CAD","ABRA","ABRA"};
    cout << "input: ";
    mw.printVector( S );
    mw.generate( S );
    cout << "PASS" << endl;
}

void test_isMagicWord()
{
    cout << "---- Test isMagicWord ----" << endl;
    MagicWords mw;
    string word;
    int K, res, exp;
    word = "ABRACADABRA";
    K = 1;
    exp = true;
    res = mw.isMagicWord( word, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    word = "CADABRAABRA";
    K = 2;
    exp = false;
    res = mw.isMagicWord( word, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    word = "ABRAABRA";
    K = 2;
    exp = true;
    res = mw.isMagicWord( word, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    word = "RAABRAAB";
    K = 2;
    exp = true;
    res = mw.isMagicWord( word, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    word = "AAAAA";
    K = 1;
    exp = false;
    res = mw.isMagicWord( word, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    cout << "PASS" << endl;
}

void test_count()
{
    cout << "---- Test count ----" << endl;
    MagicWords mw;
    vector<string> S;
    int K, res, exp;
    S = {"CAD","ABRA","ABRA"};
    K = 1;
    exp = 6;
    res = mw.count( S, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    S = {"AB","RAAB","RA"};
    K = 2;
    exp = 3;
    res = mw.count( S, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    S = {"AA","AA","AAA","A"};
    K = 1;
    exp = 0;
    res = mw.count( S, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    S = {"AA","AA","AAA","A","AAA","AAAA"};
    K = 15;
    exp = 720;
    res = mw.count( S, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    S = {"ABC","AB","ABC","CA"};
    K = 3;
    exp = 0;
    res = mw.count( S, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    S = {"A","B","C","A","B","C"};
    K = 1;
    exp = 672;
    res = mw.count( S, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    S = {"AAAAAAAAAAAAAAAAAAAA",
         "AAAAAAAAAAAAAAAAAAAA",
         "AAAAAAAAAAAAAAAAAAAA",
         "AAAAAAAAAAAAAAAAAAAA",
         "AAAAAAAAAAAAAAAAAAAA",
         "AAAAAAAAAAAAAAAAAAAA",
         "AAAAAAAAAAAAAAAAAAAA",
         "AAAAAAAAAAAAAAAAAAAB"};
    K = 1;
    exp = 40320;
    res = mw.count( S, K );
    cout << "res: " << res << " exp: " << exp << endl;
    assert( res == exp );
    cout << "PASS" << endl;
}

void test()
{
    test_generate();
    test_isMagicWord();
    test_count();
}

int main()
{
    test();
    return 0;
}
