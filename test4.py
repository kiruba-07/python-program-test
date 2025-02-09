#Reverse a integer number n
n=76542
b=len(str(n))
reverse_num=0
while(n>0):
    remainder=n%10
    reverse_num=remainder+(reverse_num*10)
    n=n//10
print(reverse_num)

