print("Welcome to FtoC, a program that converts fahrenheit input to celcius output using the equation C=5/9(F-32)")

input("Please press Enter if you wish to continue...")
Fdeg = int(input("Enter the fahrenheit temperature you wish to convert to celcius using the equation C=5/9(F-32)"))

interDeg1 = (Fdeg - 32)
print(interDeg1 * 5 / 9)
