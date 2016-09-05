"""
Author: Aadil Ahamed
4/30/2016
digits.py: Problem 1 Code Jam Round 1B
"""

MAX_LEN = 2001
digit_map = { "ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9, "TEN":10 }
digits = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN" ]

def build_map(string):
    char_map = {}
    for char in string:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map


def add_to_res(res, str_digit, freq):
    num = digit_map[str_digit]
    for i in range(freq):
        res.append(num)
    return res


def update_map(char_map, str_digit, freq):
    for char in str_digit:
        char_map[char] -= freq
        print("char:", char, "value:", char_map[char], "freq:", freq)
        assert char_map[char] >= 0
    return char_map


def phone_number(string):
    res = []
    char_map = build_map(string)
    for digit in digits:
        min_num = MAX_LEN
        for char in digit:
            num_char = 0
            if char in char_map:
                num_char = char_map[char]
            if num_char < min_num:
                min_num = num_char
        if min_num > 0:
            char_map = update_map(char_map, digit, min_num)
            add_to_res(res, digit, min_num)
    return res
        

def test_build_map():
    string = "ABCDEF"
    print(string)
    print(build_map(string))
    string = "AAABZZDDDD"
    print(string)
    print(build_map(string))


def test_add_to_res():
    res = []
    str_digit = "ONE"
    freq = 3
    res = add_to_res(res, str_digit, freq)
    print("res:", res)
    str_digit = "SIX"
    freq = 2
    res = add_to_res(res, str_digit, freq)
    print("res:", res)


def test_update_map():
    string = "ONEONETWO"
    char_map = build_map(string)
    str_digit = "ONE"
    freq = 2
    char_map = update_map(char_map, str_digit, freq)
    print("string:", string)
    print("str_digit:", str_digit, "freq:", freq)
    print("final map:", char_map)
    str_digit = "TWO"
    freq = 1
    char_map = update_map(char_map, str_digit, freq)
    print("string:", string)
    print("str_digit:", str_digit, "freq:", freq)
    print("final map:", char_map)


def test_phone_number():
    #string = "OZONETOWER"
    #print(phone_number(string))
    string = "WEIGHFOXTOURIST"
    print(phone_number(string))
    #string = "OURNEONFOE"
    #print(phone_number(string))
    #string = "ETHER"
    #print(phone_number(string))
    


def test():
    # test_build_map()
    # test_add_to_res()
    # test_update_map()
    test_phone_number()


def main():
    test()

if __name__ == "__main__":
    main()
