s = input()
res = s.split('+')
new = []
for n in res:
    new.append(n)
new.sort()
print('+'.join(new))