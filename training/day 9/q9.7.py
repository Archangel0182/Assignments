char = input("Enter a character: ")

if char.isalpha():
    if char.isupper():
        print("Uppercase alphabet")
    else:
        print("Lowercase alphabet")
else:
    print("Not an alphabet")
