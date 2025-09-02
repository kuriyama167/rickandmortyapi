name = "bob"
greeting = "Hello, {}"
with_name= greeting.format(name)

##print(with_name)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")
##print(formatted)

#name = input("Enter your name: ")
##print(name)

#size_input = input("How bgif is ypur house (in feet): ")
#square_feet = int(size_input)
#square_metres = square_feet / 10.8
##print(square_metres)
##print(f"{square_feet} square feet is {square_metres:.2f} square metres.")

#user_age = int(input("Enter your age: "))
#months = user_age * 12
##print(f"Your Age, {user_age}, is equal to {months} months ")

l = ["Bob", "Rolf", "Anne"] #list 
t = ("Bob", "Rolf", "Anne") #tuples
s = {"Bob", "Rolf", "Anne"} #sets

##l.append("Smith")
##print(l) ###

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

##local_friends = friends.difference(abroad)
##print(local_friends)

local = { "Rolf"}
abroad = {"Bob", "Anne"}

##friends = local.union(abroad)
##rint(friends)

art = {"bob", "jen", "rolf", "charlie"}
science = {"bob", "jen", "adam", "anne"}

##both = art.intersection(science)
##print(both)

##day_of_week = input("what day of the week is it today? ").lower()

#if day_of_week == "monday":
   # print("have a great start to ypur week!")

##elif day_of_week == "tuesday":
    ##print("Full speed ahead!") 

##else: 
   ## print("full speed ahead!")

##print("This always runs")
    
##The in keyword in python!!!!!!!!!!!!

movies_watched = {"the matrix", "green book", "her"}
##user_movie = input("enter something yopu have watched recenlty:").lower()

##print(user_movie in movies_watched)


number = 7 
user_input = input("Enter 'y' if yoyu wannna play : ").lower

if user_input == "y": 
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You won!")
    elif abs(number - user_number) == 1: 
        print
    else:
        print("sorry trry again! ")
