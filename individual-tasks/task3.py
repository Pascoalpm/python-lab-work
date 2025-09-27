# task3.py - Triangle Area (Heron's Formula)
import math

print("=== Triangle Area Calculation (Heron's Formula) ===")

try:
	a = float(input("Enter side a: "))
	b = float(input("Enter side b: "))
	c = float(input("Enter side c: "))

	if a + b > c and a + c > b and b + c > a:
		p = (a + b + c) / 2
		s = math.sqrt(p * (p - a) * (p - b) * (p - c))

		print(f"\n--- Results ---")
		print(f"Side a: {a}")
		print(f"Side b: {b}")
		print(f"Side c: {c}")
		print(f"Semi-perimeter (p): {p:.2f}")
		print(f"Area of ​​triangle: {s:.2f}")
	else:
		print("❌ Error: The sides do not form a valid triangle!")

except ValueError:
	print("⚠️ Please enter valid numbers!")