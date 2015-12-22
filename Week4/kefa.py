"""
kefa.py
"""


def kefa(a):
    length = max_length = i = 1
    while i < len(a):
        if a[i] >= a[i-1]:
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 1
        i += 1
    if length > max_length:
        max_length = length
    return max_length


def main():
    a = [2, 2, 1, 3, 4, 1]
    print kefa(a)
    a = [9, 8, 7, 6]
    print kefa(a)
    a = [1, 2, 3, 4]
    print kefa(a)


if __name__ == '__main__':
    main()
