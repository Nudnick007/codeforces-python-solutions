s = input()
mean = s.split('WUB')
res = ''
for n in mean:
    if n!='':
        res += ' '+ n
print(res[1:])