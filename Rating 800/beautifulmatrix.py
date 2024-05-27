# 0 0 0 0 0
# 0 0 0 0 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
#center belongs to nums[2][2]
nums = []
for i in range(5):
    nums.append(list(map(int,input().split())))
for i in range(5):
    for j in range(5):
        if nums[i][j] == 1:
            r = i
            c = j
            break
#r = 1, j=4 op = 3
print(abs(r-2)+abs(c-2))