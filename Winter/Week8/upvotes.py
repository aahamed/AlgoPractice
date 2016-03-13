"""
Author: Aadil Ahamed
upvotes.py: Quora challenge
"""

import random
import time
from collections import deque

"""
naive_ndec: Count the number of non-decreasing subranges in a given window (naive)
"""
def naive_ndec(array, start, window):
        end = start + window - 1
        count = 0
        for i in range(start, end):
                j = i
                while(j <= end-1):
                        if array[j] <= array[j+1]:
                                count += 1
                        else:
                                break
                        j += 1
        return count


"""
naive_ninc: Count the number of non-increasing subranges in a given window (naive)
"""
def naive_ninc(array, start, window):
        end = start + window - 1
        count = 0
        for i in range(start, end):
                j = i
                while(j <= end-1):
                        if array[j] >= array[j+1]:
                                count += 1
                        else:
                                j += 1
                                break
                        j += 1
        return count


"""
ndec_v2: Count the number of non-decreasing subranges in a given window (version 2)
"""
def ndec_v2(array, start, window):
        end = start + window - 1
        count = 0
        i = start
        while(i <= end-1):
                j = 0
                while(i+j <= end-1):
                        if array[i+j] <= array[i+j+1]:
                                count += j + 1
                                j += 1
                        else:
                                j += 1
                                break
                i += j
        return count


"""
ninc_v2: Count the number of non-increasing subranges in a given window (version 2)
"""
def ninc_v2(array, start, window):
        end = start + window - 1
        count = 0
        i = start
        while(i <= end-1):
                j = 0
                while(i+j <= end-1):
                        if array[i+j] >= array[i+j+1]:
                                count += j + 1
                                j += 1
                        else:
                                j += 1
                                break
                i += j
        return count

"""
nchoose2: Compute the value of n choose 2
"""
def nchoose2(n):
        return (n*(n-1))//2

"""
num_ranges: Determine the number of subranges based on the seq_list
"""
def num_ranges(seq_list):
        count = 0
        for seq in seq_list:
                seq_length = seq[1] - seq[0] + 1
                count += nchoose2(seq_length)
        return count

"""
ndec_top: Top level algorithm for ndec - first pass
"""
def ndec_top(array, start, window):
        init = final = start
        seq_list = deque()
        for final in range(start, start + window - 1):
                if array[final] <= array[final + 1]:
                        pass
                else:
                        seq_list.append([init, final])
                        init = final+1
        final += 1
        if final >= init:
                seq_list.append([init, final])
        return seq_list

"""
ndec: Count the number of non-decreasing subranges in a given window (version 3)
"""
def ndec(array, start, window, seq_list=None, prev_num=0):
        curr_num = prev_num     # number of decreasing sub-ranges
        if (seq_list == None) or (len(seq_list) == 0):
                # assert start == 0
        if start == 0:
                seq_list = ndec_top(array, start, window)
                curr_num = num_ranges(seq_list)
        else:
                first_seq = seq_list.popleft()
                if first_seq[0] == start - 1 and first_seq[1] > first_seq[0]:
                        curr_num -= (first_seq[1] - first_seq[0])   #seq_length reduces by 1 -> curr_num reduces by n-1
                        first_seq[0] = start
                        seq_list.appendleft(first_seq)

                end = start + window - 1
                if array[end - 1] <= array[end]:
                        last_seq = seq_list.pop()
                        last_seq[1] = end
                        curr_num += (last_seq[1] - last_seq[0])    #seq_length increases by 1 -> curr_num increases by 1
                        seq_list.append(last_seq)
                else:
                        seq_list.append([end, end])
        return (curr_num, seq_list)

"""
ninc_top: Top level algorithm for ninc - first pass
"""
def ninc_top(array, start, window):
        init = final = start
        seq_list = deque()
        for final in range(start, start + window - 1):
                if array[final] >= array[final + 1]:
                        pass
                else:
                        seq_list.append([init, final])
                        init = final+1
        final += 1
        if final >= init:
                seq_list.append([init, final])
        return seq_list

"""
ninc: Count the number of non-increasing subranges in a given window (version 3)
"""
def ninc(array, start, window, seq_list=None, prev_num=0):
        curr_num = prev_num
        if (seq_list == None) or (len(seq_list) == 0):
                assert start == 0
        if start == 0:
                seq_list = ninc_top(array, start, window)
                curr_num = num_ranges(seq_list)
        else:
                first_seq = seq_list.popleft()
                if first_seq[0] == start - 1 and first_seq[1] > first_seq[0]:
                        curr_num -= (first_seq[1] - first_seq[0])   #seq_length reduces by 1 -> curr_num reduces by n-1
                        first_seq[0] = start
                        seq_list.appendleft(first_seq)

                end = start + window - 1
                if array[end - 1] >= array[end]:
                        last_seq = seq_list.pop()
                        last_seq[1] = end
                        curr_num += last_seq[1] - last_seq[0]     #seq_length increases by 1 -> curr_num increases by 1
                        seq_list.append(last_seq)
                else:
                        seq_list.append([end, end])
        return (curr_num, seq_list)


"""
metric_v1: Compute upvotes metric version 1
"""
def     metric_v1(array, window):
        N = len(array)
        res = []
        for i in range(0, N - window + 1):
                non_dec = naive_ndec(array, i, window)
                non_inc = naive_ninc(array, i, window)
                res.append((non_dec - non_inc))
                #print (non_dec - non_inc)
        return res


"""
metric: Compute upvotes metric version 2
"""
def metric(array, window):
        N = len(array)
        bounds = [(-window * (window - 1))/2, (window * (window - 1))/2]
        res = []
        num_dec = num_inc = 0
        ndec_seq_list = None
        ninc_seq_list = None
        for i in range(0, N - window + 1):
                (num_dec, ndec_seq_list) = ndec(array, i, window, ndec_seq_list, num_dec)
                (num_inc, ninc_seq_list) = ninc(array, i, window, ninc_seq_list, num_inc)
                # assert (num_dec - num_inc) >= bounds[0] and (num_dec - num_inc) <= bounds[1]
                res.append(num_dec - num_inc)
                # print(num_dec - num_inc)
        return res

"""
test_ndec: Unit test for ndec()
"""
def test_ndec():
        print("Testing ndec")
        a = [1, 2, 3]
        res = ndec(a, 0, len(a))
        exp = 3
        exp_list = deque([[0,2]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list
        a = [3, 1, 1]
        res = ndec(a, 0, len(a))
        exp = 1
        exp_list = deque([[0,0], [1, 2]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list
        a = [2, 3, 1, 1]
        res = ndec(a, 0, len(a))
        exp = 2
        exp_list = deque([[0, 1], [2, 3]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list
        a = [1, 2, 3, 1]
        seq_list = deque([[0, 2]])
        window = 3
        res = ndec(a, 1, window, seq_list, 3)
        exp = 1
        exp_list = deque([[1, 2], [3, 3]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list


"""
test_ninc: Unit test for ninc()
"""
def test_ninc():
        print("Testing ninc")
        a = [1, 2, 3]
        res = ninc(a, 0, len(a))
        exp = 0
        exp_list = deque([[0,0], [1, 1], [2, 2]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list
        a = [3, 1, 1]
        res = ninc(a, 0, len(a))
        exp = 3
        exp_list = deque([[0, 2]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list
        a = [2, 3, 1, 1]
        res = ninc(a, 0, len(a))
        exp = 3
        exp_list = deque([[0, 0],[1, 3]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list
        a = [1, 2, 3, 1]
        seq_list = deque([[0, 0], [1, 1], [2, 2]])
        window = 3
        res = ninc(a, 1, window, seq_list)
        exp = 1
        exp_list = deque([[1, 1], [2,3]])
        print("res:",res, "exp:",(exp, exp_list))
        assert res[0] == exp
        assert res[1] == exp_list


"""
test_metric: Unit test for metric()
"""
def test_metric():
        print("Testing metric")
        a = [1, 2, 3, 1, 1]
        window = 3
        res = metric(a, window)
        exp = [3, 0, -2]
        print("res:", res, "exp:", exp)
        assert res == exp
        a = [1, 2, 3, 1, 1]
        window = 4
        res = metric(a, window)
        exp = [2, -1]
        print("res:", res, "exp:", exp)
        assert res == exp
        a = [9, 5]
        window = 2
        res = metric(a, window)
        exp = metric_v1(a, window)
        print("res:", res, "exp:", exp)
        assert res == exp
        # a = [random.randint(0, 1000000000) for i in range(100000)]
        a = [7, 15, 3, 1, 0, 9, 1, 14, 2, 2]
        window = 3
        start = time.time()
        res = metric(a, window)
        end = time.time()
        exp = metric_v1(a, window)
        #print("res:", res)
        #print("exp:", exp)
        assert res == exp
        print(end - start)

def main():
        #(N, K) = map(int, raw_input().split(" "))
        #array = map(int, raw_input().split(" "))
        #metric(array, K)
        #test_ndec()
        #test_ninc()
        test_metric()


if __name__ == "__main__":
        main()
