x = 0
t = int(input())
for _ in range(t):
    s = input()
    if s[1] == '+':
        x+=1
    else:
        x-=1
print(x)