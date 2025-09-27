# individual.py - Temperature Conversion
print("=== Temperature Conversion ===")

celsius = float(input("Temperature in Celsius: "))

# Conversions
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f"\n--- Results ---")
print(f"Celsius: {celsius:.2f}°C")
print(f"Fahrenheit: {fahrenheit:.2f}°F")
print(f"Kelvin: {kelvin:.2f}K")