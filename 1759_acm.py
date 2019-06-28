alpha = [0]*26

def hasleastone(l):
    u = 0
    n = 0
    for a in l:
        if a is 'a' or a is 'e' or a is 'i'or a in 'o' or a is 'u': u+=1
        else: n+=1
    return u,n

def go(l, v, index, count, n, m):
    if count == n:
        (u,n) = hasleastone(v)
        if u>=1 and n>=2:
            print(''.join(v))
        return
    elif count < n and index >= m:
        return
    else:
            
        v.append(l[index])
        go(l,v,index+1,count+1,n,m)
        v.remove(l[index])
        go(l,v,index+1,count,n,m)    


for i in range(0,26):
    alpha[i] = 0

n, m = list(map(int,input().split()))

v= []
l  = list(input().split())
l.sort()
go(l,v,0,0,n,m)
