#global ans
inf = -10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(1, n+1):
    t[i],p[i] = map(int,input().split())
ans = 0

def go(day, s, max0):

    if day == n+1:
        max0 = max(max0, s)
        return
    if day > n+1:
        return
    go(day+1, s,max0)
    go(day+t[day], s+p[day], max0)
    return

max0 = 0
go(1, 0, max0)
print(max0)