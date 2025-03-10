def separate_squares(start, end):
    squares = [num ** 2 for num in range(start, end + 1)]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    return even_squares, odd_squares

start, end = eval(input("Enter start of range and end seperated by a comma : "))

even_squares, odd_squares = separate_squares(start, end)

print("Even squares:", even_squares)
print("Odd squares:", odd_squares)