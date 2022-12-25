import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters
key = list(chars)
random.shuffle(key)

while True:
    user_input = input("Enter the message to Encrypt or message to Decrypt or q to Quit: ").lower()

    if user_input == "encrypt":
        plain_text = input("Enter message to Encrypt: ")
        temp = ""
        for i in plain_text:
            index_no = chars.index(i)
            temp += key[index_no]
        print(f"Original message: {plain_text}")
        print(f"Encrypted message: {temp}")

    elif user_input == "decrypt":
        plain_text = input("Enter message to Decrypt: ")
        temp = ""
        for i in plain_text:
            index_no = key.index(i)
            temp += chars[index_no]
        print(f"Encrypted message: {plain_text}")
        print(f"Original message: {temp}")

    elif user_input == "q" or user_input == "quit":
        print("Thanks for using this Encrypt or Decrypt message program")
        break
    else:
        print("Invalid command. Please try again.")
        user_input = input(
            "Enter the text to Encrypt or Code To Decrypt and q to Quit : ")
