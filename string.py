a = input().lower()
b = input().lower()
for i in range(len(a)):
    if ord(a[i]) < ord(b[i]):
        print(-1)
        c = 0
        break
    elif ord(a[i]) > ord(b[i]):
        print(1)
        c = 0
        break
    else :
        c = 1
if c == 1 :
    print(0)








