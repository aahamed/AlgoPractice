# Author: Aadil Ahamed
# palindrome.py: Topcoder palindrome problem

class Palindrome( object ):

  def isPalindrome( self, string, splitPt, estLen ):
    for i in range( splitPt, len(string) ):
      if string[i] != string[estLen - 1 - i]:
        return False
    return True

  def find( self, string ):
    N = len(string)
    for splitPt in range( N/2, N ):
      if string[splitPt] == string[splitPt-1]:
        estLen = splitPt * 2
        if self.isPalindrome(string, splitPt, estLen):
          return estLen
      else:
        estLen = splitPt * 2 + 1
        if self.isPalindrome(string, splitPt, estLen):
          return estLen


def testIsPalindrome():
  print "---- Test isPalindrome() ----"
  p = Palindrome()
  s = "abcd"
  splitPt = 2
  estLen = 5
  exp = False
  res = p.isPalindrome( s, splitPt, estLen )
  print "res:", res, "exp:", exp
  assert res==exp
  s = "abcb"
  splitPt = 2
  estLen = 5
  exp = True
  res = p.isPalindrome( s, splitPt, estLen )
  print "res:", res, "exp:", exp
  assert res==exp
  s = "abbd"
  splitPt = 2
  estLen = 4
  exp = False
  res = p.isPalindrome( s, splitPt, estLen )
  print "res:", res, "exp:", exp
  assert res==exp
  s = "abba"
  splitPt = 2
  estLen = 4
  exp = True
  res = p.isPalindrome( s, splitPt, estLen )
  print "res:", res, "exp:", exp
  assert res==exp
  s = "abcde"
  splitPt = 4
  estLen = 9
  exp = True
  res = p.isPalindrome( s, splitPt, estLen )
  print "res:", res, "exp:", exp
  assert res==exp
  s = "abbbbb"
  splitPt = 3
  estLen = 6
  exp = False
  res = p.isPalindrome( s, splitPt, estLen )
  print "res:", res, "exp:", exp
  assert res==exp


def testFind():
  print "---- Test find() ----"
  p = Palindrome()
  s = "abcd"
  exp = 7
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp 
  s = "abcb"
  exp = 5
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp 
  s = "abbd"
  exp = 7
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp 
  s = "abba"
  exp = 4
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp 
  s = "abcde"
  exp = 9
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp 
  s = "abbbbb"
  exp = 8
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp

def provTests():
  print "---- Provided Tests ----"
  p = Palindrome()
  s = "abab"
  exp = 5
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp
  s = "abacaba"
  exp = 7
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp
  s = "qwerty"
  exp = 11
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp
  s = "abdfhdyrbdbsdfghjkllkjhgfds"
  exp = 38
  res = p.find(s)
  print "res:", res, "exp:", exp
  assert res==exp



def test():
  testIsPalindrome()
  testFind()
  provTests()


def main():
  test()

if __name__ == "__main__":
  main()

