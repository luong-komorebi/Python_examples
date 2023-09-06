q=0
n=int(input("Enter Number: "))
while (n>0):
 r=n%10
 q=q+r
 n //= 10
print(f"Sum of digits is: {str(q)}")
