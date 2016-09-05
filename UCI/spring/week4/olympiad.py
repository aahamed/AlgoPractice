"""
Author: Aadil Ahamed
ACM Week 4
olympiad.py
"""

def create_set(i, n, array):
    curr_set = []
    for j in range(n):
        if (i & (1 << j)) > 0:
            # add jth problem to curr set
            curr_set.append(array[j])
    return curr_set

def is_valid(curr_set, l, r, x):
    total_sum = sum(curr_set)
    max_dif = max(curr_set)
    min_dif = min(curr_set)
    check1 = total_sum >= l and total_sum <= r
    check2 = (max_dif - min_dif) >= x
    return check1 and check2

def count_sets(n, l, r, x, array):
    num_sets = 2 ** n
    count = 0
    for i in range(1, num_sets):
        curr_set = create_set(i, n, array)
        if is_valid(curr_set, l, r, x):
            count += 1
    return count

def test():
    pass

def main():
    n, l, r, x = list(map(int, input().split(" ")))
    array = list(map(int, input().split(" ")))
    print(count_sets(n, l, r, x, array))

if __name__ == "__main__":
    main()
