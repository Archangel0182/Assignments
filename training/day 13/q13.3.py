def remove_punctuation():
    string = input("Enter a string: ")
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for char in string:
        if char in punctuation:
            string = string.replace(char, '')

    print("String without punctuation:", string)


remove_punctuation()
