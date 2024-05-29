import sys
input = sys.stdin.readline
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
n = inp()
nums = inlt()

l = 0
mx = 0 
for r in range(n):
    while l < r and nums[r] < nums[r - 1]:
            l += 1
    mx = max(mx, r - l + 1)
print(mx)
        