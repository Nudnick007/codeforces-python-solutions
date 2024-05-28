s = input()
flag = False
for ch in s:
    if ch=='H' or ch=='Q' or ch=='9':
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')