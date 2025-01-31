num = int(input("Enter any number:"))
binary_num = ""

if num==0:
    binary_num = "0"
else:
    while num>0:
        binary_num =  str(num%2) + binary_num
        num = num//2

print(f"binary number is: {binary_num}")