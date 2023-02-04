a = int(input())
if a == 0:
    print(0)
else:
    f = 0
    fn = 1
    n = 1
    b = -1
    while fn <= a:
        if fn == a:
            b = n
        f, fn = fn, f + fn
        n += 1
print(b)
