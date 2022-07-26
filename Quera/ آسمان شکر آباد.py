x = input()
x = x.split(" ")
n = int(x[0])
m = int(x[1])
ans = 0
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == "*":
            ans += 1

print(ans)