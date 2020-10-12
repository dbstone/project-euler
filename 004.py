# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

max_palindrome = 0

def is_palindrome(n):
    return str(n)[::-1] == str(n)

for i in range(100, 1000):
    for j in range(i, 1000):
        n = i * j
        if is_palindrome(n):
            # print(i, j)
            max_palindrome = max(max_palindrome, n)

print(max_palindrome)
