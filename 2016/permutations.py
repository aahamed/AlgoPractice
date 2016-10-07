import pdb

def generate( n, A ):
    if n == 1:
          print A
    else:
        i = 0
        while True:
            generate(n - 1, A)
            if i == (n - 1):
                break
            if n % 2 == 0:
                A[i], A[n-1] = A[n-1], A[i]
            else:
                A[0], A[n-1] = A[n-1], A[0]
            i = i + 1

def main():
    pdb.set_trace()
    ls = [1, 2, 3]
    generate( len(ls), ls )

if __name__ == '__main__':
    main()
