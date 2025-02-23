valid = False 
while not valid:
    try:
        age = int(input("Enter your age: "))  # Ensure input is integer
        valid = True  # Input is valid, exit loop
        if age % 2 == 0:
            print(f"Your age {age} is an even number.")
        else:
            print(f"Your age {age} is an odd number.")
    except ValueError:
        print("Make sure to enter an integer.")