"""
Author: Aadil Ahamed
Date: 3/12/16
candies.py: Hackerrank problem Candies
"""

def num_candies(i, C, R):
    lb1 = lb2 = 0

    # Special Case 1 -> 1st element
    if i == 0:
        if R[i] > R[i+1]:
            C[i] = num_candies(i+1, C, R) + 1
        else:
            C[i] = 1
        return C[i]

    # Special Case 2 -> last element
    if i == len(C) - 1:
        if R[i] > R[i-1]:
            C[i] = C[i-1] + 1
        else:
            C[i] = 1
        return C[i]

    # General Case
    if R[i] <= R[i-1] and R[i] <= R[i+1]:
        C[i] = 1
        return 1
    if R[i] > R[i-1]:
        lb1 = C[i-1]
    if R[i] > R[i+1]:
        C[i+1] = num_candies(i+1, C, R)
        lb2 = C[i+1]
    C[i] = max(lb1, lb2) + 1
    return C[i]

def min_candies(R):
    N = len(R)
    C = [-1 for i in range(N)]
    for i in range(N):
        if C[i] == -1:
            num_candies(i, C, R)
    return sum(C)

def test_min_candies():
    R = [1, 2, 2]
    res = min_candies(R)
    exp = 4
    print("res:", res, "exp:", exp)
    assert(res == exp)

    R = [2, 2, 1]
    res = min_candies(R)
    exp = 4
    print("res:", res, "exp:", exp)
    assert(res == exp)

    R = [9, 8, 7, 1, 2, 3, 2, 1]
    res = min_candies(R)
    exp = 18
    print("res:", res, "exp:", exp)
    assert(res == exp)

def main():
    # test_min_candies()
    N = int(input())
    R = []
    for i in range(N):
        R.append(int(input()))
    print(min_candies(R))

if __name__ == "__main__":
    main()
