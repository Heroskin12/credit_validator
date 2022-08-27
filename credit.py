# Prep Step - Define digit sum function for us in Step 1.
def digitsum(n):
    sum0 = 0
    while (n != 0):
        sum0 += (n % 10)
        n = n // 10
    return sum0

# Get user input.
number = input("Enter your credit card number: ")
strnumber = str(number)
length = len(strnumber)
# print(f"{length}")

# Step 1: 
# - Multiply every other number by 2, starting with the one before last number.
# - Add together the digits of those numbers.
# - The conditions of the for loop depend on size of length.
sum1 = 0

if length % 2 == 0: # even
    for i in range(length-2, -1, -2):
        digits = int(strnumber[i]) * 2
        sum1 += digitsum(digits)
else: # odd
    for i in range(length-2, 0, -2):
        digits = int(strnumber[i]) * 2
        sum1 += digitsum(digits)
# print(f"{sum1}")

# Step 2: Add every other number together.
sum2 = 0

if length % 2 == 0: # even
    for i in range(length-1, 0, -2):
        sum2 += int(strnumber[i])
else: # odd
    for i in range(length-1, -1, -2):
        sum2 += int(strnumber[i])
# print(f"{sum2}")

# Step 3: Add sums together.
sum1 += sum2
#print(f"{sum1}")

# Step 4: Check if final digit is 0. If it does, continue with other checks.
if (sum1 % 10) != 0:
    print("INVALID")

elif length == 15:
    print("AMEX")

elif length == 13:
    print("VISA")
    
elif length == 16:
    if strnumber[0] == "5":
        print("MASTERCARD")
    elif strnumber[0] == "4":
        print("VISA")