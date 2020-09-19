first_string = input("Give the first string: ")
second_string = input("Give the second string: ")

formatted_String = "\"{}\"".format(second_string)
print("Replaced string: ", first_string.replace(second_string, formatted_String))



