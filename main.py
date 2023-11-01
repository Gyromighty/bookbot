with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(f"{len(words)} words found in the document\n")
    letter_counts = {}
    letter_list = []
    for letter in file_contents:
        if letter.isalpha():
            letter_counts[letter.lower()] = letter_counts.get(letter.lower(), 0) + 1
    letter_list = list(letter_counts.items())
    letter_list.sort(key=lambda letter: letter[1], reverse=True)
    
    
    for letter in letter_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")