# Sunny number  # math.isqrt
import math

def is_perfect_square(n):
    root = math.isqrt(n)
    val = root * root
    if val == n:
        return True
    else:
        return False

num = 24
if is_perfect_square(num+1):
    print(f'{num} is Sunny Number')
else:
    print(f'{num} is not Sunny Number ')