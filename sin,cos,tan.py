import math 
angle = float(input("Enter an angle in degrees: "))
radians = math.radians(angle)
sin_val = math.sin(math.radians(angle))
cos_val = math.cos(math.radians(angle))
tan_val = math.tan(math.radians(angle))
print("sin(", angle, ") =", sin_val)
print("cos(", angle, ") =", cos_val)
if cos_val != 0:
    print("tan(", angle, ") =", tan_val)
else:
    print("tan(", angle, ") is undefined (division by zero).")