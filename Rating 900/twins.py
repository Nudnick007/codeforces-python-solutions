n = int(input())
lst = list(map(int,input().split()))
lst = sorted(lst,reverse=True)
half = sum(lst)//2
cur = 0
cnt = 0
for n in lst:
    cur +=n
    cnt+=1
    if cur>half:
        break
print(cnt)