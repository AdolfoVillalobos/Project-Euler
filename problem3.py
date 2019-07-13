from sympy.ntheory import isprime

N = 600851475143


def largest_prime(N):

    current = N
    list = []
    for i in range(1, N):
        if isprime(i):
            if N%i==0:
                list.append(i)
                current /= i
                if current == 1:
                    break
        else:
            continue
    return max(list)

print(largest_prime(2**(50)))
