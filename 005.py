import timeit
from math import gcd

# LCM via GCD
def lcm2(a, b):
    return abs(a * b) // gcd(a, b)

# slow, iterative LCM
def lcm(a, b):
    val = 0
    big = max(a, b)
    small = min(a, b)
    while True:
        val += big
        if val % small == 0:
            return val

# solve with commutative property of LCM
def solve():
    last = 11
    for i in range(12, 21):
        last = lcm2(last, i)
    
    return last

print(solve())

task = 'solve()'
print(f'exec time: {timeit.timeit(task, globals=globals(), number=100_000) * 10} μs')

def gabe():
    Not_found = True
    ahhh = 2560

    while Not_found:
        if ahhh % 11 == 0:
            if ahhh % 12 == 0:
                if ahhh % 13 == 0:
                    if ahhh % 14 == 0:
                        if ahhh % 15 == 0:
                            if ahhh % 16 == 0:
                                if ahhh % 17 == 0:
                                    if ahhh % 18 == 0:
                                        if ahhh % 19 == 0:
                                            Not_found = False
                                        else:
                                            ahhh += 20
                                    else:
                                        ahhh += 20
                                else:
                                    ahhh += 20
                            else:
                                ahhh += 20
                        else:
                            ahhh += 20
                    else:
                        ahhh += 20
                else:
                    ahhh += 20
            else:
                ahhh += 20
        else:
            ahhh += 20
    return ahhh

# gabe()
# task = 'gabe()'
# print(f'exec time: {timeit.timeit(task, globals=globals(), number=10) / 10} s')