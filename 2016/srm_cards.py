"""
Author: Aadil Ahamed
srm_cards.py: TopCoder Problem 
"""

class SRMCards(object):

    def maxTurns(self, array):
        mTurns = 0
        i = 0
        array = sorted(array)
        while i < len(array) - 1:
            if array[i+1] == array[i] + 1:
                i += 2
            else:
                i += 1
            mTurns += 1
        if i == len(array) - 1:
            mTurns += 1
        return mTurns



def test():
    s = SRMCards()
    array = [498, 499]
    exp = 1
    res = s.maxTurns(array)
    print("res:", res, "exp:", exp)
    assert res == exp
    array = [491, 492, 495, 497, 498, 499]
    exp = 4
    res = s.maxTurns(array)
    print("res:", res, "exp:", exp)
    assert res == exp
    array = [100, 200, 300, 400]
    exp = 4
    res = s.maxTurns(array)
    print("res:", res, "exp:", exp)
    assert res == exp
    array = [11, 12, 102, 13, 100, 101, 99, 9, 8, 1]
    exp = 6
    res = s.maxTurns(array)
    print("res:", res, "exp:", exp)
    assert res == exp
    array = [118, 321, 322, 119, 120, 320]
    exp = 4
    res = s.maxTurns(array)
    print("res:", res, "exp:", exp)
    assert res == exp
    array = [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    exp = 7
    res = s.maxTurns(array)
    print("res:", res, "exp:", exp)
    assert res == exp


def main():
    test()


if __name__ == "__main__":
    main()
