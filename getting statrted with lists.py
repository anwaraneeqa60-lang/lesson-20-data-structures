lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
even_squares = []
odd_squares = []
for num in range(lower_limit, upper_limit + 1):
    square = num ** 2
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print(f"\nEven Squares: {even_squares}")
print(f"Odd Squares: {odd_squares}")