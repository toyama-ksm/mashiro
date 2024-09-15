user_year = int(input())
if user_year%4==0 and user_year%100!=0 or user_year%400==0:
    print("Y")
else :
    print("N")
