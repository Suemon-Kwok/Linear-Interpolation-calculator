def linear_interpolation():
    # Take user inputs
    Max_given_a = float(input("Enter value for Max_given_a: "))
    M_given_b = float(input("Enter value for M_given_b: "))
    X_given_Z = float(input("Enter value for X_given_Z: "))
    Max_given_A2 = float(input("Enter value for Max_given_A2: "))
    Max_given_B2 = float(input("Enter value for Max_given_B2: "))

    # Calculate the left side of the equation
    left_side = (Max_given_a - M_given_b) / (Max_given_a - X_given_Z)

    # Rearrange the right side of the equation to solve for Y_given_W
    Y_given_W = Max_given_A2 - ((Max_given_A2 - Max_given_B2) / left_side)

    return Y_given_W

# Repeat function
while True:
    # Call the function and print the result
    Y_given_W = linear_interpolation()
    print("The interpolated value Y_given_W is: ", Y_given_W)

    # Ask the user if they want to interpolate again
    repeat = input("Do you want to interpolate again? (yes/no): ")
    if repeat.lower() != "yes":
        break
