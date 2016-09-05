"""
Author: Aadil Ahamed
ropestring.py: Topcoder programming problem
"""

DOT = '.'
DASH = '-'

class Ropestring(object):

    def reconstruct(self, ropes):
        res = ''
        for i in range(len(ropes)):
            for j in range(ropes[i]):
                res += DASH
            if i < len(ropes)-1:
                res += DOT
        return res

    def makerope(self, s):
        even = []
        odd = []
        num_spaces = 0
        rope_len = 0
        res = ''
        for i in range(len(s)):
            if s[i] == DOT:
                num_spaces += 1
                if rope_len == 0:
                    continue
                elif rope_len % 2 == 0:
                    even.append(rope_len)
                else:
                    odd.append(rope_len)
                rope_len = 0
            elif s[i] == DASH:
                rope_len += 1
            else:
                print("Invalid Character")
        if rope_len > 0:
            if rope_len % 2 == 0:
                even.append(rope_len)
            else:
                odd.append(rope_len)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        odd_str = self.reconstruct(odd)
        even_str = self.reconstruct(even)
        if len(even_str) > 0 and len(odd_str) > 0:
            res = even_str + DOT + odd_str
            num_spaces -= (len(even) + len(odd) - 1)
        elif len(even_str) > 0:
            res = even_str
            num_spaces -= (len(even)-1)
        elif len(odd_str) > 0:
            res = odd_str
            num_spaces -= (len(odd)-1)
        for i in range(num_spaces):
            res += DOT
        return res



def test():
    rs = Ropestring()
    s = "..-..-"
    exp = "-.-..."
    res = rs.makerope(s)
    print("res:", res, "exp:", exp)
    assert res == exp
    s = "-.-"
    exp = "-.-"
    res = rs.makerope(s)
    print("res:", res, "exp:", exp)
    assert res == exp
    s = "--..-.---..--"
    exp = "--.--.---.-.."
    res = rs.makerope(s)
    print("res:", res, "exp:", exp)
    assert res == exp
    s = "--..-.---..--..-----.--."
    exp = "--.--.--.-----.---.-...."
    res = rs.makerope(s)
    print("res:", res, "exp:", exp)
    assert res == exp
    s = "..."
    exp = "..."
    res = rs.makerope(s)
    print("res:", res, "exp:", exp)
    assert res == exp



def main():
    test()

if __name__ == "__main__":
    main()
