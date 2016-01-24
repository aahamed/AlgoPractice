"""alena.py"""


def alena(array):
    i = 0
    counter = 0
    num_pairs = 0
    while array[i] == 0:
        i += 1
    for j in range(i, len(array)):
        if array[j] == 0:
            counter += 1
        elif array[j] == 1:
            if counter == 1:
                num_pairs += 2
            else:
                num_pairs += 1
            counter = 0
    return num_pairs
