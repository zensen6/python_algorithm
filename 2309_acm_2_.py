l = []
sum = 0
exec(9*"l+=[int(input())];")
exec("for i in l: sum+=i")
l.sort()
done = False
for i in l:
    for j in l:
        if i is not j and sum-i-j==100:
            l.remove(i); l.remove(j); done = True; break
    if done is True: break

for i in l: print(i)