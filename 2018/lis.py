# 159 173 13 68 190 95 126 66 84 140
S = [ 10, 22, 9, 33, 21, 50, 41, 60, 80 ]
n = len( S )
L = [ 0 ] * n

print "S:", S

def lis2( seq, i ):
    if i == 0:
        L[ i ] = 1
        #print "i:", i, "L:", L
        return 1
    maxLis = 1
    for j in range( i ):
        if seq[ j ] < seq[ i ]:
            if L[ j ]:
                jLis = L[ j ]
            else:
                jLis = lis( seq, j )
            if jLis >= maxLis:
                maxLis = jLis + 1
    L[ i ] = maxLis
    #print "i:", i, "L:", L
    return maxLis

def lis( seq ):
    n = len( seq )
    L = [ 0 ] * n
    for i in range( n ):
        maxLis = 1
        for j in range( i ):
            if seq[ j ] < seq[ i ]:
                if L[ j ] >= maxLis:
                    maxLis = L[ j ] + 1
        L[ i ] = maxLis
        print "i:", i, "L:", L
    return L[ n-1 ]


print "LIS:\n", lis( S )
