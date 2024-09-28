#Task 1
while True:
    try:
        temp = float(input("Enter the temperature in fahrenheit: "))
#Task 2
        celsius = (temp - 32) * 5/9
    except ValueError:
        print("Please only use numbers for your input. Try again. ")
#Task 3
    else:
        print(f"{temp} degrees Fahremheit is {celsius} degrees Celsius.")
#Task 4
    finally:
        print("Thank you for using the weather forecast application.")