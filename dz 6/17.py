from math import sqrt

x = int(input())
s = 0
n = 0
q = 0

while x != 0:
    s += x
    q += x ** 2
    x = int(input())
    n += 1

print(sqrt((q - s ** 2 / n) / (n - 1)))