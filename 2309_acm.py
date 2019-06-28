arr = [0]*9
brr = [0]*7

sum = 0
for i in range(0,9):
    arr[i] = int(input())
    sum += arr[i]

done = False

for i in range(0,9-1):
    for j in range(i+1,9):
        if sum-arr[i]-arr[j] is 100:
            index1 = i
            index2 = j
            done = True
            break
    if done==True:
        break

bindex = 0

for k in range(0,9):
    if k is not index1 and k is not index2:
        brr[bindex] = arr[k]
        bindex+=1

brr.sort()
for i in brr:
    print(i)