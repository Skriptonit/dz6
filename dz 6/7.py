sum = 0
c = 0
len = 0
element = int(input())
while element != 0:
    len += 1
    sum += element
    element = int(input())
    c = (sum / len) * 1.0

print(c)