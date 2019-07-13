## Recursive adding is too slow. We will save intermediate sums in ouputs.
def fib(n, computed={0:0, 1:1}):
        if n not in computed:
                computed[n] = fib(n-1, computed)+fib(n-2, computed)
        return computed[n]


actual_fib = 0
current = 0
sum = 0

while actual_fib <= 4000000:
    actual_fib =fib(current)
    if actual_fib % 2 == 0:
        sum += actual_fib
    current += 1

print(sum)
