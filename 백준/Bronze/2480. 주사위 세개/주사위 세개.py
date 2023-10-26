a, b, c = map(int, input().split())

if a == b == c:
    reward = 10000 + a * 1000
elif a == b or a == c:
    m = a
    reward = 1000 + m * 100
elif b == c:
    m = b
    reward = 1000 + m * 100
else:
    m = max(a, b, c)
    reward = m * 100
# a != b != c를 사용하면 a == c인 경우를 포함하게 됨

print(reward)
