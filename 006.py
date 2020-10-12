N = 100

squared_sum = (N * (N+1) / 2) ** 2

def sum_of_squares(n):
    s = 0
    x = []
    for i in range(1, n+1):
        x.append(s)
        s += i*i
    return s

def sum_of_squares2(n):
    return (n**3)/3 + -(n**2)/2 + n/6

print(squared_sum - sum_of_squares2(N))

# an^3 + bn^2 + cn + d

# a1^3 + b1^2 + c1 + d = 0
# a2^3 + b2^2 + c2 + d = 1
# a3^3 + b3^2 + c3 + d = 5
# a4^3 + b4^2 + c4 + d = 14

# (n^3)/3 + -(n^2)/2 + n/6
