vowels = ['a','e','i','o','u','y']

s = input()
s = s.lower()
res = ''
for ch in s:
    if ch not in vowels:
        res += '.' + ch
print(res)