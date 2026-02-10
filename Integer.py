try:
    num=int(input("Enter a number: "))
    print("number: ", num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print("You entered a valid number.")
finally:
    print("Execution completed.")
