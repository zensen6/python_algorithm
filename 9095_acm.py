T = int(input())

#l = []
#for i in range(0,T):
#    l.append(int(input()))
l = []
exec(T*"l.append(int(input()));")

count = 0
c = 0
while c<T:
    for l1 in range(1,3+1):
        if l1 is l[c]: count+=1
        for l2 in range(1,3+1):
            if l1+l2 is l[c]: count+=1
            for l3 in range(1,3+1):
                if l1+l2+l3 is l[c]: count+=1
                for l4 in range(1,3+1):
                    if l1+l2+l3+l4 is l[c]: count+=1
                    for l5 in range(1,3+1):
                        if l1+l2+l3+l4+l5 is l[c]: count+=1
                        for l6 in range(1,3+1):
                            if l1+l2+l3+l4+l5+l6 is l[c]: count+=1
                            for l7 in range(1,3+1):
                                if l1+l2+l3+l4+l5+l6+l7 is l[c]: count+=1
                                for l8 in range(1,3+1):
                                    if l1+l2+l3+l4+l5+l6+l7+l8 is l[c]: count+=1
                                    for l9 in range(1,3+1):
                                        if l1+l2+l3+l4+l5+l6+l7+l8+l9 is l[c]: count+=1
                                        for l10 in range(1,3+1):
                                            if l1+l2+l3+l4+l5+l6+l7+l8+l9+l10 is l[c]: count+=1
    c+=1
    print(count)
    count = 0