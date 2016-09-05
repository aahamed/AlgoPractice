"""
Lottery.py
"""


def is_balanced(freq_list):
    key = freq_list[0]
    for i in range(1, len(freq_list)):
        if freq_list[i] != key:
            return False
    return True


def lottery(k, array):
    count = 0
    freq_list = [0 for _ in range(k)]
    for elem in array:
        freq_list[elem-1] += 1
    while not(is_balanced(freq_list)):
        ind_max = freq_list.index(max(freq_list))
        ind_min = freq_list.index(min(freq_list))
        freq_list[ind_max] -= 1
        freq_list[ind_min] += 1
        count += 1
    return count


def test_lottery():
    array = [2, 1, 2, 2]
    k = 2
    exp_res = 1
    res = lottery(k, array)
    print 'res:', res, 'exp:', exp_res
    array = [1, 2, 1, 1, 1, 4, 1, 4]
    k = 4
    exp_res = 3
    res = lottery(k, array)
    print 'res:', res, 'exp:', exp_res


def main():
    test_lottery()

main()
