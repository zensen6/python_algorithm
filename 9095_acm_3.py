def go (sum, goal):
    if sum > goal: return 0
    if sum is goal: return 1

    now = 0
    for i in range(1,3+1):
        now += go(sum+i,goal)
    return now

T = int(input())
while T>0:
    T-=1
    n = int(input())
    print(go(0,n))