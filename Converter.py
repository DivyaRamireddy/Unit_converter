converter.pydef km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462


print("⚙️  Smart Unit Converter ⚙️\n")
print("Choose a conversion type:")
print("1. Kilometers ↔ Miles")
print("2. Celsius ↔ Fahrenheit")
print("3. Kilograms ↔ Pounds")

choice = input("\nEnter your choice (1/2/3): ")

if choice == '1':
    num = float(input("Enter value: "))
    direction = input("Convert (K→M / M→K): ").upper()
    if direction == 'K→M':
        print(f"{num} km = {km_to_miles(num):.2f} miles")
    else:
        print(f"{num} miles = {miles_to_km(num):.2f} km")

elif choice == '2':
    num = float(input("Enter value: "))
    direction = input("Convert (C→F / F→C): ").upper()
    if direction == 'C→F':
        print(f"{num}°C = {celsius_to_fahrenheit(num):.2f}°F")
    else:
        print(f"{num}°F = {fahrenheit_to_celsius(num):.2f}°C")

elif choice == '3':
    num = float(input("Enter value: "))
    direction = input("Convert (K→P / P→K): ").upper()
    if direction == 'K→P':
        print(f"{num} kg = {kg_to_pounds(num):.2f} pounds")
    else:
        print(f"{num} pounds = {pounds_to_kg(num):.2f} kg")

else:
    print("❌ Invalid choice.")
