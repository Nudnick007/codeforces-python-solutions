s = input()
# max_1 = 0
# max_0 = 0
# cnt_1 = 0
# cnt_0 = 0
# for ch in s:
#     if ch=='1':
#         cnt_1 +=1
#         max_1 = max(max_1,cnt_1)
#         cnt_0 = 0
#     elif ch=='0':
#         cnt_0 +=1
#         max_0 = max(max_0,cnt_0)
#         cnt_1 = 0
# if max_1 >= 7 or max_0 >=7:
#     print('YES')
# else:
#     print('NO')

if '0000000' in s or '1111111' in  s:
    print('YES')
else:
    print('NO')