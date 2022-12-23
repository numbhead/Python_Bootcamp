def greet():
    print("Welcome to the Club. You may enter")

def nope():
    print("This is an unautorized space for you. Please leave!")

password = "Python Rocks"
user_input = input("What is the password?")
if(user_input == password):
    greet()
else:
    nope()