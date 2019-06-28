def next_permutation(a,n):
    i = n-1
    while i>0 and a[i-1] >= a[i]: i-=1
    if i<=0: return False
    j = n-1
    while a[i-1] >= a[j]: j-=1
    a[i-1],a[j] = a[j],a[i-1]
    a[i:] = reversed(a[i:])
    return True

n = int(input())
l = list(map(int,input().split(' ')))

l = sorted(l)

sum0 = 0; max0 = 0
for i in range(1,n):
    sum0 += abs(l[i-1]-l[i])
max0 = max(max0,sum0)
sum0 = 0

while next_permutation(l,n):
    sum0 = 0
    for i in range(1,n):
        sum0 += abs(l[i-1]-l[i])
    max0 = max(max0,sum0)

print(max0)