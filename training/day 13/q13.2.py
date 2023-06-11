def count_stats():
    string = input("Enter a string: ")
    word_count = len(string.split())
    char_count = len(string)
    space_count = string.count(' ')

    print("Number of words:", word_count)
    print("Number of characters:", char_count)
    print("Number of spaces:", space_count)


count_stats()
