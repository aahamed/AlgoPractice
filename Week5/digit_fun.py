__author__ = 'aahamed'

def digit_fun(a0):
    a_prev = int(a0)
    i = 1
    while(True):
        a_next = len(str(a_prev))
        if(a_next == a_prev):
            return i
        else:
            i += 1
            a_prev = a_next

def main():
    a0 = input()
    while(a0 != 'END'):
        print(digit_fun(a0))
        a0 = input()


main()
