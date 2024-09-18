leg = int(input())
if leg % 4 == 0 :
    print (int(leg / 4) , int(leg / 2))
if leg % 4 != 0 and leg % 2 == 0:
    print (int(leg // 4 +1) , int (leg / 2))
if leg % 2 != 0 :
    print (0,0)


