import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
mini = float('inf')

for i in range(n, m+1):
    mini = min(mini, abs(arr[i-1] - arr[i-n]))

print(mini)
