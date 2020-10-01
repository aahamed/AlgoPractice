inputStr = raw_input()
print "input:", inputStr
n = len( inputStr )
reverseStr = [ inputStr[ n -1 - i ] \
        for i in range( n ) ]
reverseStr = "".join( reverseStr )
print "reversed:", reverseStr

