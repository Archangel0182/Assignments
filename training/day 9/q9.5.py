char = input("Enter a character: ").lower()

if char.isalpha():
    if char in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
