# numbers.py - Operations with four numbers
print("=== Operations with Four Numbers ===")

try:
	# Request four numbers
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	num3 = float(input("Enter the third number: "))
	num4 = float(input("Enter the fourth number: "))

	# Calculate sums
	sum1 = num1 + num2
	sum2 = num3 + num4

	# Calculate division
	if sum2 != 0:
		result = sum1 / sum2
		# Display result with 2 decimal places
		print(f"\n--- Results ---")
		print(f"Sum of the first two: {sum1}")
		print(f"Sum of the last two: {sum2}")
		print(f"Division of the sums: {result:.2f}")
	else:
		print("❌ Error: Division by zero!")

except ValueError:
	print("⚠️ Please enter valid numbers!")

