import string

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_letters = get_chars(book_text)
    book_wordcount = get_wordcount(book_text)
    print("A book summary")
    print(f"{book_wordcount} words are in the book")
    only_alpha(book_letters)


    
    
    
    #print(book_text)
    #print(get_wordcount(book_text))
    #print(get_chars(book_text))
    

def get_book_text(path):
    with open(path) as f:
        return f.read() 

def get_wordcount(text):
    return len(text.split())

def get_chars(text):
    lowercase_book = text.lower()
    character_count = {}
    for char in lowercase_book:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def only_alpha(dict):
    for letter in dict:
        if letter.isalpha():
            print(f"the '{letter}' occurs {dict[letter]} times")
    return



main()