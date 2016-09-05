"""
Author: Aadil Ahamed
Created: 6/5/16
max_subarray.py: Find the maximum possible sum of a contiguous subarray
"""

def max_sub(A):
    m_sum = A[0]
    i = 0
    while i < len(A) and A[i] <= 0:
        if A[i] > m_sum:
            m_sum = A[i]
        i += 1

    if i >= len(A):
            return m_sum
    m_sum = 0
    for j in range(i, len(A)):
        if A[j] > 0:
            m_sum += A[j]
    return m_sum

def max_sum(A):
    N = len(A)
    memo = [0 for i in range(N)]
    memo[0] = A[0]
    for j in range(1, N):
        memo[j] = max( memo[j-1] + A[j], A[j] )
    
    return max(memo)


def test1():
    a = [2, -1, 2, 3, 4, -5]
    exp = 10
    res = max_sum(a)
    print("max sum =", res, "exp =", exp)
    assert(res == exp)
    a = [-4, -5, 2, 3, -1, 5]
    exp = 9
    res = max_sum(a)
    print("max sum =", res, "exp =", exp)
    assert(res == exp)


def test2():
    a = [-1, -2, 1, -3]
    exp = 1
    res = max_sum(a)
    print("max sum =", res, "exp =", exp)
    assert(res == exp)
    a = [-5]
    exp = -5
    res = max_sum(a)
    print("max sum =", res, "exp =", exp)
    assert(res == exp)


def test3():
    a = [2, -1, 2, 3, 4, -5]
    exp = 11
    res = max_sub(a)
    print("max sub =", res, "exp =", exp)
    assert(res == exp)
    a = [-1, -2, 1, -3]
    exp = 1
    res = max_sub(a)
    print("max sub =", res, "exp =", exp)
    assert(res == exp)
    a = [-5]
    exp = -5
    res = max_sub(a)
    print("max sub =", res, "exp =", exp)
    assert(res == exp)


def test():
    test1()
    test2()
    test3()


def main():
    # test()
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split(" ")))
        print(max_sum(A), max_sub(A))


if __name__ == "__main__":
    main()
