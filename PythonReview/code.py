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

##while True:
       ## user_input = input("Would u like to play? (Y/n) ")
        ##if user_input == "n":
            ## break

        ##user_number = int(input("Guess our number: "))
        ##if user_number == number:
           ## print("You won!")
        ##elif abs(number - user_number) == 1: 
          ##  print
       ## else:
         
         ##   print("sorry trry again! ")



friends = ["yesser", "humberto", "carlos", "jeff", "kenia"]
starts_s=[]
##for friend in friends:

for friend in friends: 
    if friend.startswith("h"):
        starts_s.append(friend)

#rint(starts_s)
#print(friends)
#print(friends is starts_s)
#print("friends: ", id(friends), "starts_s", id(starts_s))
##Allthough the list has the same values doesnt mean they are equal cause theya re suaing a diffecrten memory direcccion but is we compare
##just the elemets beetween then they are going to be the same , no the same list though

friend_ages = {"Jeff": 27, "Clara": 24 , "Kevin": 33 }

friend_ages["Jeff"]= 28 ##the elemtn in the dictionary 


##print(friend_ages);


friends = [
    {"name" : "kevin", "age": 33}, 
    {"name" : "Clara", "age": 24}, 
    {"name" : "Jeff", "age": 27}, 
]

##print(friends[1]["name"]) ##acesss a specifit data in a dicticionary


student_attendance = {"Clara": 90, "jeff": 97 , "kevin": 78}

##for student, attendance in student_attendance.items():  access to a values in loop 
   ## print(f"{student} : {attendance}")

people = [("bod", 42, "Musician"), ("james", 24, "Artist"), ("Harry", 32 , "Lecturer")]

###for name, age, profession in people:  we need create a cvariabl ef ro easch elemt in the duples 
   ##print(f"Name: {name}, Age:{age}, Profession : {profession}")


#person = ("james", 24, "Artist")

#name, _, profession= person

##print(name, profession) ## to ignore a data in python


#*head, tail = [1, 2, 3, 4, 5]

#print(*head)
#print(tail)


##def user_age_in_days():
   ## user_age = int(input("Enter your age: "))
    ##age_days = user_age * 365
    ##print(f"Your Age in days: {age_days}.")

##user_age_in_days()
#friends = ["Rolf", "Bob"]

#def add_friend():
   ##friend_name = input("Enter the name: ")
   
   #friends.append(friend_name)

#add_friend() 
#print(friends)

#def say_hello(name):
   #print(f"Hello, {name}")

#say_hello("meow")



##def divide(dividend, divisor):
  ##  if divisor != 0:
  ##      return dividend / divisor
  ## else: 
      ##  return "You Fool!"
    
##result = divide(15, 2) * 5

#rint(result)



##########################################Lamba functions 
##sequence = [1, 3, 5, 9]
#doubled = [(lambda x:x*2)(x)for x in sequence]
##oubled = list(map(lambda x: x*2, sequence))
##print(doubled)

#########List comprernesion ###################
################################################################password and user confirmation 
##users = [
   # (0, "Bob", "password"), 
    #(1, "Rolf", "bob123"), 
    #(2, "Jose", "longpassjopse"), 
    #(3, "username", "Passwor12")
#]

#username_mapping = {user[1]: user for user in users}

#username_input = input("Enter your username: ")
#password_input = input("Enter your password: ")

#_, username, password = username_mapping[username_input]

#if password_input == password: 
   # print("Your details are correct")
#else:
   # print("your details are incorrect")


#Unpacking with kwargs and args
##def named(**kwargs):
    #print(kwargs)

##details = {"name": "bob", "age": 25}

#named(**details)###

def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
         print(f"{arg}: {value}")

print_nicely(name="bob", age=25, city="new york")