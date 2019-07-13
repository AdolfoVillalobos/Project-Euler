

## naive aproach
def sum_divisors(N):
    list = []
    for t in range(1,N):
        if (t%3==0) or (t%5==0):
            list.append(t)
    return sum(set(list))

## Faster Aproach: Overlap
def sum_divisors_fast(N):
    a = obtain_max(3, N)
    b = obtain_max(5, N)
    c = N//(3*5)

    return int(3*n_first(a)+5*n_first(b)-(3*5)*n_first(c))

def obtain_max(p, n):
    if n % p == 0:
        return (n/p-1)
    else:
        return n//p

def n_first(n):
    return n*(n+1)/2
%%time
print(sum_divisors_fast(1000000))

%%time
print(sum_divisors(1000000))
