""""
duff_meat.py
"""


def duff_meat(a, p):
    amt_meat = 0
    money_spent = 0
    i = 0
    while i < len(a):
        amt_meat += a[i]
        j = i+1
        while j < len(a) and (p[j] > p[i]):
            amt_meat += a[j]
            j += 1
        money_spent += amt_meat * p[i]
        i = j
        amt_meat = 0
    return money_spent


def main():
    a = [1, 2, 3, 1, 3, 4]
    p = [7, 3, 6, 6, 1, 4]
    print duff_meat(a, p)
    a = [1, 2, 3]
    p = [3, 2, 1]
    print duff_meat(a, p)
    a = [1, 2, 3]
    p = [3, 1, 2]
    print duff_meat(a, p)


if __name__ == '__main__':
    main()


