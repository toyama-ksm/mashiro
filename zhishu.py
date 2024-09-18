num = (int(input()) , int(input()))
sma = min(num)
big = max(num)
for x in range(sma , big+1 ) :
    for i in range (2 , x ) :
        if x % i == 0 :
            break
    else :
        print(f'{x}是素数')


