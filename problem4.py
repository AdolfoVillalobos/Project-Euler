
def is_palindrome(N):
    S = str(N)
    return S == S[::-1]


def find(n):

    upperbound = 10**(2*(n))-1
    lowerbound = 10**(2*(n-1))
    print(upperbound)
    print(lowerbound)

find(3)
