import timeit

# O(n)
def solve1():
    total = 0
    x = 3
    while x < 1000:
        total += x
        x += 3

    x = 5
    while x < 1000:
        if x % 3 != 0:
            total += x
        x += 5
    
    return total

# O(n)
def solve2():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    
    return total

# O(1)
def solve3():
    def sum_multiples(n):
        N = 999 // n
        return n * N * (N + 1) / 2
    
    return int(sum_multiples(3) + sum_multiples(5) - sum_multiples(15))

print(f'Answer: {solve3()}')

task = 'solve1()'
print(f'Solution 1 exec time: {timeit.timeit(task, globals=globals(), number=10_000) * 100} μs')
task = 'solve2()'
print(f'Solution 2 exec time: {timeit.timeit(task, globals=globals(), number=10_000) * 100} μs')
task = 'solve3()'
print(f'Solution 3 exec time: {timeit.timeit(task, globals=globals(), number=1_000_000)} μs')


