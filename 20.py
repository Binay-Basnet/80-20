import random

s = [1000 for y in range(1000)]
# this function paly game of life
def play(i, j):
    p = random.randint(0, 1)
    if p == 0:
        s[i] -= 10
        s[j] += 10
    else:

        s[j] -= 10
        s[i] += 10


# this loop through life
for i in range(90000000):
    x = random.randint(0, 999)
    if s[x] == 0:
        continue
    y = random.randint(0, 999)
    if s[y] == 0:
        continue
    play(x, y)

s.sort()
d = 0
e = 0
for i in range(799):
    d = d + s[i]

for i in range(799, 999):
    e = e + s[i]

print("rest 80 percent", d)
print(d / (1000 * 1000))
print("top 20 percent", e)
print(e / (1000 * 1000))

for i in range(999):
    print(s[i])
