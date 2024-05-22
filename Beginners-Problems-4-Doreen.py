#NAME LOOP
name=(input("What is your name?")) 
number=int(input("Choose a number."))
for num in range(number): 
  print(name)
  
#PASSWORD CHECKER
right=False
while not right: 
  password=input("Enter your password.") 
  if password=="meow": 
    right=True 
    print("prrrrr, you got the password right :3") 
  elif password=="woof": 
    right=False 
    print("BARK BARK!") 
  else: print("WRONG.")

#MULTIPLICATION TABLE
multiplier=int(input("Please enter a positive interger. I'll tell you the multiplication table up to 10 :)"))

for number in range(11):
    print(number*multiplier)
    
print("You're welcome!")

#PRIME NUMBER CHECKER
userNumber=int(input("Please input an integer. I will tell you if it is a prime number or not."))

notPrime = False
if userNumber == 1:
    print(userNumber, "is not a prime number")
elif userNumber > 1:
    for i in range(2, userNumber):
        if (userNumber % i) == 0:
            notPrime = True

    if notPrime:
        print(userNumber, "is not a prime number")
    else:
        print(userNumber, "is a prime number")



