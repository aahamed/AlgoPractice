__author__ = 'aahamed'
"""
hindex.py
"""


def is_h_index(h, gt, lt, eq):
    if gt == h:
        return True
    elif gt > h:
        return False
    else:
        if gt + eq >= h:
            return True


def h_index(array):
    n = len(array)
    h = 0
    for i in range(n):
        k = array[i]
        gt = 0
        lt = 0
        eq = 0
        for j in range(n):
            if i != j:
                if array[j] > k:
                    gt += 1
                if array[j] < k:
                    lt += 1
        eq = n - gt - lt
        if is_h_index(k, gt, lt, eq):
            h = k
    return h


class HIndex(object):

    def is_hindex(self, h, gt, eq):
        if gt == h:
            return True
        if gt > h:
            return False
        if gt < h:
            if gt + eq >= h:
                return True
            else:
                return False

    def h_index(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        h_tmp = h = 0
        index = 0
        n = len(citations)
        while h_tmp <= n and index < n:
            while citations[index] < h_tmp:
                index += 1
            if citations[index] > h_tmp:
                gt = n - index
                eq = 0
                if self.is_hindex(h_tmp, gt, eq):
                    h = h_tmp
                h_tmp += 1
            elif citations[index] == h_tmp:
                gt = n - index - 1
                eq = 1
                if self.is_hindex(h_tmp, gt, eq):
                    h = h_tmp
                index += 1
        return h

    def h_index2(self, citations):
        n = len(citations)
        distribution = [0 for i in range(n+1)]
        for num_citations in citations:
            if num_citations < n:
                distribution[num_citations] += 1
            else:
                distribution[n] += 1
        lt = 0
        for dummy_h in range(n+1):
            eq = distribution[dummy_h]
            gt = n - lt - eq
            if self.is_hindex(dummy_h, gt, eq):
                h = dummy_h
            lt += eq
        return h



def main():
    a = [9, 3, 4, 5, 7, 12, 6]
    b = [4, 2, 2, 2, 2]
    c = [100, 100, 100]
    print h_index(a)
    print HIndex().h_index(b)
    print HIndex().h_index(b)


if __name__ == "__main__":
    main()
