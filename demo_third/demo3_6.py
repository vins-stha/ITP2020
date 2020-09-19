A = input("Give the string A: ")
B = input("Give the string B: ")

first_index = A.index(B)  #index of first occurrence 
strlen = len(B)# start position = firs_index + len(B)

print("The index of the 2nd occurrence of B in A is {}.".format(A.find(B, first_index+strlen, len(A))))
