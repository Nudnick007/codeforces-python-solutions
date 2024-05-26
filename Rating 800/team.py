t = int(input())
cnt = 0
for _ in range(t):
    a,b,c = map(int, input().split())
    if a+b+c >=2:
        cnt+=1
print(cnt)