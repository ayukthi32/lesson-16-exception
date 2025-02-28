#acp
def check_age():
    age = input("Please enter your age: ")
    if age.isdigit() == False:
        print("Error: Age should be a positive integer.")
        return
    age = int(age)
    if age % 2 == 0:
        print(f"The age {age} is an even number.")
    else:
        print(f"The age {age} is an odd number.")
check_age()