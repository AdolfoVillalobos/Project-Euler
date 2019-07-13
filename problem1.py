N = 1000

def sum_divisors(N):
    list = []
    for t in range(1,N):
        if (t%3==0) or (t%5==0):
            list.append(t)
    return sum(set(list))

print(sum_divisors(1000))
