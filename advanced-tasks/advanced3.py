# advanced3.py - Sum of 3- and 2-Digit Numbers (without conditionals)
print("=== Sum of 3- and 2-Digit Numbers ===")

try:
    # Input the individual digits
    print("Enter the digits of the 3-digit number:")
    a3 = int(input("Hundreds (a3): "))
    a2 = int(input("Tens (a2): "))
    a1 = int(input("Units (a1): "))

    print("Enter the digits of the 2-digit number:")
    b2 = int(input("Tens (b2): "))
    b1 = int(input("Units (b1): "))

    # Calculate sum digit by digit
    units_sum = a1 + b1
    carry1 = units_sum // 10
    result_units = units_sum % 10

    tens_sum = a2 + b2 + carry1
    carry2 = tens_sum // 10
    result_tens = tens_sum % 10

    result_hundreds = a3 + carry2

    # Display results
    print(f"\n--- Results ---")
    print(f"3-digit number: {a3}{a2}{a1}")
    print(f"2-digit number: {b2}{b1}")
    print(f"\nDigits of the sum:")
    print(f"Hundreds: {result_hundreds}")
    print(f"Tens: {result_tens}")
    print(f"Units: {result_units}")
    print(f"Final result: {result_hundreds}{result_tens}{result_units}")

except ValueError:
    print("Please enter valid integers!")