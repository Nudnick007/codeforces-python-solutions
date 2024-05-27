first = input()
second = input()
first = first.lower()
second = second.lower()
if first==second:
    print(0)
for i in range(len(first)):
    if ord(second[i]) > ord(first[i]):
        print(-1)
        break
    elif ord(first[i]) > ord(second[i]):
        print(1)
        break