def count_vowels():
    string = input("Enter a string: ")
    vowels = 'aeiou'
    vowel_count = {}.fromkeys(vowels, 0)

    for char in string.lower():
        if char in vowel_count:
            vowel_count[char] += 1

    print("Vowel Counts:")
    for vowel, count in vowel_count.items():
        print(vowel, ":", count)


count_vowels()