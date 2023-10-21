h, m = map(int, input().split())

if m < 45:
    m1 = 45 - m
    m = 60 - m1
    if h != 0:
        h -= 1
    elif h == 0:
        h = 23

else:
    m = m - 45

print(h, m)