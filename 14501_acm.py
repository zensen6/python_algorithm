inf = -10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(1, n+1):
    t[i],p[i] = map(int,input().split())
ans = 0
def go(index, s):
    global ans
    if index == n+1:
        ans = max(ans, s)
        return
    if index > n+1:
        return
    go(index+1, s)
    go(index+t[index], s+p[index])

go(1, 0)
print(ans)