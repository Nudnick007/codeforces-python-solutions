n, k = map(int,input().split())
cnt = 0
lst = list(map(int,input().split()))
val = lst[k-1]
for i in range(len(lst)):
    if lst[i] >= val and lst[i]>0:
        cnt+=1
    else:
        break
print(cnt)