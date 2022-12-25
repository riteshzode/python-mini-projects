# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid


# get the credit card number from this website to check the program
# https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm
# step 1

card_number = input("Enter a credit card #: ")

card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number.replace("\t", "")

card_number = card_number[::-1]

# print(card_number[::2])
# print(card_number[1::2])

# step 2

sum_odd_digit = sum(int(x) for x in card_number[::2])

# step 3

sum_even_digit = sum((1 + (int(x) * 2 % 10) if int(x) * 2 > 10 else int(x) * 2 for x in card_number[1::2]))

# step 4

total = sum_odd_digit + sum_even_digit

# step 5

if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")