from math import sqrt

a = int( input(" Input values for a : "))
b = int(input(" Input values for b : "))
c = int(input(" Input values for c : "))

root = (b*b - 4*a*c)
if root >= 0: #check if square root can be calculated
    x1= (-b + sqrt(root))/(2*a) 
    x2= (-b - sqrt(root))/(2*a)
    
print("roots : \n %.1f \n %.1f" %(x1,x2))