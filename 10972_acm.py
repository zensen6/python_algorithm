def next_permutation(a,n):
    i = n-1
    while i>0 and a[i-1] >= a[i]: i-=1
    if i<=0: return False
    j = n-1
    while a[j] <= a[i-1]: j-=1
    a[i-1],a[j] = a[j],a[i-1]
    '''
    j = n-1
    while i<j:
        a[i],a[j] = a[j],a[i]
        i+=1; j-=1 
    '''
    a[i:] = reversed(a[i:])
    return True


n = int(input())
a = list(map(int,input().split(' ')))

#sorted(a, key= lambda x:a[4:7],reverse = True) 안됨

if next_permutation(a,n)==True: 
    for i in a: print(i,end=' ')
else: print(-1)

