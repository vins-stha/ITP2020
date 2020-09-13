from datetime import date 

name = input("Give your name : ")
year = int (input("Which year you were born : ")) #get year as int
current_year = int(date.today().strftime("%Y"))  #get current year as int
if year > current_year: #check if entered year exists 
    print("Are you from future ?")
else:
    print("Hello, %s. You are %d years in %d " %(name,(current_year - year ),current_year))