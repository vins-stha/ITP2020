mystring = input("Give a string: ")
vowels = ['a','e','i','o','u']
count = 0
# for  in range(0,len(mystring)):
for lettr in mystring:
    if lettr in vowels:
        count = count+1
a = mystring.count('a')
e = mystring.count('e')
i = mystring.count('i')
o = mystring.count('o')
u = mystring.count('u')

print("Number of vowels: ",a+e+i+o+u)
    