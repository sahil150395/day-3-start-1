print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        # print("Please pay $5")
    elif age <= 18:
        bill = 7
        # print("Please pay $7")
    elif age >=45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        # print("Please pay $12")
    
    photos = input("Do you want photos? (Yes/No) ")
    if photos == "Yes":
        bill += 3
    
    print(f"Total bill: {bill}")
else:
    print("You can't ride the rollercoaster!")

