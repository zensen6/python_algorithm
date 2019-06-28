'''

def next_permutation(a,n):
    i = n-1
    while i>0 and a[i-1] >= a[i]: i-=1
    if i<=0: return False
    j = n-1
    while a[i-1] >= a[j]: j-=1
    a[i-1],a[j] = a[j],a[i-1]
    a[i:n] = reversed(a[i:n])
    return True

n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

l = [i for i in range(0,n)]
l.append(0)
min0 = 999999999


while True:
    notdone = False 
    l[n] = l[0]
    sum0 = 0
    for i in range(0,n):
        if arr[l[i]][l[i+1]] is 0:
            notdone = True
            break
        else:
            sum0 += arr[l[i]][l[i+1]]
    if notdone is False: min0 = min(min0,sum0)
    if next_permutation(l,n) == False: break

print(min0)

'''

def permutation(D,n):
    i=n-1
    while D[i-1]>=D[i]:
        i-=1
    if i<=0:
        return False
    j=n-1
    while D[i-1]>=D[j]:
        j-=1
    D[i-1],D[j]=D[j],D[i-1]
    j=n-1
    while i<j:
        D[i],D[j]=D[j],D[i]
        i+=1;j-=1
    return True

N=int(input())
D=[i for i in range(N)]
cost=[];ans=10*10**6
for i in range(N):
    cost.append([*map(int,input().split())])
while 1:
    if D[0]!=0:break
    err=0; k=0; price=cost[D[N-1]][D[0]]
    if price==0:break
    else:k+=price
    for i in range(N-1):
        price=cost[D[i]][D[i+1]]
        if price==0:err=1;break
        k+=price
    if err==0 and ans>k:ans=k
    permutation(D,len(D))
print(ans)