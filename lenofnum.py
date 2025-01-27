num = int(input("Enter a number:"))
leng = 0

if num == 0:
    print("The number you have entered is negative please try again!")
else:
    while num > 0:
        num = num//10
        leng = leng + 1
    print(leng)