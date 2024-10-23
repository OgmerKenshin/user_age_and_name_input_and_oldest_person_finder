# set conditions for valid name (alphabet letters and spaces only) and valid ages (numbers between 0-122) and return
# insert an array to store names and ages
# while true loop for user inputs
# while not statement for name 
# print("HAHA wrong!!!)
# while not statement for age
# print("seriously? invalid age dude...")
# conver age = int(age)
# retry input("do you wanna input another entry? (yes or no):")
# if oldest = get oldest person(array)
# else print("no valid entries")




# I'm gonne set rules for what names are valid and what names aren't
# lets allow special characters in the name too now
def is_valid_name(name):
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .'-~,")
    return all(char in allowed_characters for char in name)

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 122

# I need to account for the possibility of multiple oldest people
# I will return the age and name for the "oldest person"
def get_oldest_person(data):
    if len(data) == 0:
        return []
    oldest_age = max(person[1] for person in data)
    return [person for person in data if person [1] == oldest_age]


# Now the array is where the names and ages are stored
#this will be the array
Identification = []

#I can now proceed to making loops and user input texts
while True:
    name = input("please enter your name here: ")
    while not is_valid_name(name):
        print("HAHA wrong!!!")
        name = input("please enter your name here: ")


    age = input("please enter your age here: ")
    while not is_valid_age(age):
        print("seriously? invalid age dude...")
        age = input("please input your age here: ")

    # the age variable needs to be an integer and both variables are now stored in the array set earlier
    age = int(age)
    Identification.append((name,age))

    #retry and finally the break
    retry = input("do you wanna input another entry? (Yes or No): ").strip().lower()
    if retry != "yes": 
        break


# find and reveal the oldest person
oldest = get_oldest_person(Identification)
if oldest:
    print("The oldest people are: ")
    for person in oldest:
      print(f"{person[0]} with {person[1]}")

else: 
    print("No valid entries")
       
            

        
            
        
          