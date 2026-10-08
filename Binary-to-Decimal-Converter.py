
print("Binary to Decimal Converter")
print("---------------------------")

binary = input("Enter a binary number: ")

# Validate binary input
if all(bit in "01" for bit in binary):
    decimal = int(binary, 2)

    print("\nResult:")
    print("Binary :", binary)
    print("Decimal:", decimal)
else:
    print("Invalid input! Please enter only 0 and 1.")
