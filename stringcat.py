#define function that takes first and last name and adds them to statement
def helloMyDude(name1,name2):
    print("Hello, My name is " + name1 + ", " + name2)

# take in first and last name from user
firstname = input("please enter your first name ")
lastname = input("please enter your last name ")
#call function and pass it the names
helloMyDude(firstname, lastname)
