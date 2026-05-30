def reverse_text(text):
    rev = ""
    for i in text:
        rev = i + rev
    return rev
def count_vowels(text):
    vowels = 0
    for i in text:
        if i in "aeiouAEIOU":
            vowels += 1
    return vowels