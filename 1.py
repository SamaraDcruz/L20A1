print("Enter a number:")
try:
    num = int(input())   # user must enter a number
    print("You've entered:", num)
except ValueError:
    print("Oops! That was not a number. Please enter digits only.")