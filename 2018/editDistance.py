def editDistance2( s1, s2, len1, len2 ):
    assert len1 <= len2
    minDist = 0
    if len1 == 0:
        minDist = len2
    elif s1[ len1 - 1 ] == s2[ len2 - 1 ]:
        minDist = editDistance( s1, s2, len1-1, len2-1 )
    else:
        if len1 == len2:
            minDist = 1 + editDistance( s1, s2, len1-1, len2-1 )
        else:
            minDist = 1 + min( editDistance( s1, s2, len1, len2-1 ), editDistance( s1, s2, len1-1, len2-1 ) )
    print "s1:", s1[ :len1 ], "s2:", s2[ :len2 ], "dist:", minDist
    return minDist

def editDistance( s1, s2 ):
    len1 = len( s1 )
    len2 = len( s2 )
    dp = [ [ 0 ] * ( len2+1 ) for _ in range( len1+1 ) ]
    for i in range( len1+1 ):
        for j in range( len2+1 ):
            if i == 0:
                dp[ i ][ j ] = j
            elif j == 0:
                dp[ i ][ j ] = i
            elif s1[ i-1 ] == s2[ j-1 ]:
                dp[ i ][ j ] = dp[ i-1 ][ j-1 ]
            else:
                dp[ i ][ j ] = 1 + min( dp[ i ][ j-1 ], dp[ i-1 ][ j ], dp[ i-1 ][ j-1 ] )
            print "s1:", s1[ :i ], "s2:", s2[ :j ], "dist:", dp[ i ][ j ]
    return dp[ len1 ][ len2 ] 
            

def driver( s1, s2 ):
    len1 = len( s1 )
    len2 = len( s2 )
    if len1 < len2:
        return editDistance( s1, s2, len1, len2 )
    else:
        return editDistance( s2, s1, len2, len1 )


s1 = 'satur'
s2 = 'sun'
print "edit dist:\n", editDistance( s1, s2 )
