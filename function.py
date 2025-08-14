#function 
def square(no):
    return no ** 2

number = int(input("Enter a number:"))
result = square(number)
print("Squared value:", result)

#lambda function
no = lambda x: x**2
print(no(2))