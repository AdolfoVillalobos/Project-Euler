import numpy as np
import math
import string
from tqdm import tqdm


def base_range(start, end, base, step=1):

    def Convert(n, base):
        string = "0123456789ABCDEF"
        if n < base:
            return string[n]
        else:
            return Convert(n // base, base) + (string[n % base])
    return (Convert(i, base) for i in range(start, end, step))


def get_digits(n, base):
    return [n] if int(n) < base else get_digits(int(n / base), base) + [n % base]


def check_condition(n, base):

    result = False

    digits = get_digits(n, base)

    if len(digits) > 1:
        suma = sum(digits)

        try:
            max_n = int(math.log(n, suma))

            for i in range(1, int(math.log(n, suma)) + 1):
                power = suma**i

                if suma**i == n:
                    result = True
                    break
        except ZeroDivisionError:
            print(" ")

    return result


def find(maximo, b):

    base_iterator = base_range(1, maximo, b)
    result = []

    for i in tqdm(base_iterator, total=maximo):

        cond = check_condition(int(i), b)
        if cond:
            result.append(i)
            print(i)

    return result


if __name__ == "__main__":

    B = 10
    maximo = 10**(100)
    result = find(maximo, B)
    print(result)
