a=[]
for i in range(5):
   n=float(input("enter a float number:"))
   a.append(n)
print(a)
#prime number or not
n=int(input("enter a number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not prime number")
            break
            
    else:
            print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")



