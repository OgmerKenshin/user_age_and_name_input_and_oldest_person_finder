
# I'm gonne set rules for what names are valid and what names aren't
def valid_name(name):
    return name.replace("","").isalpha()
def valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 122
# I will return the age and name for the "oldest person"
def oldest_user(data):
    if len(data) == 0:
        return None, None
    oldest_user = max(data, key=lambda person: person[1])
    return oldest_user











#this will be the array
Identification = {}

       
            

        
            
        
          