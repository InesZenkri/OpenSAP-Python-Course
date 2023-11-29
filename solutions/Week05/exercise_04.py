def encrypt_letter(letter, key):
    if not letter.isalpha():
        return letter

    position = ord('a' if letter.islower() else 'A')
    shifted = (ord(letter) - position + key) % 26 + position
    return chr(shifted)

def calculate_shifts(letter):
    return ord(letter.lower()) - ord('a')

def encrypt_text(text, keyword):
    text = text.lower()
    keyword = keyword.lower()
    encrypted_text = ""
    counter = 0

    for char in text:
        shift = calculate_shifts(keyword[counter])
        encrypted_text += encrypt_letter(char, shift)
        counter = (counter + 1) % len(keyword)

    return encrypted_text

text_input = input("Which text should be encrypted: ")
keyword_input = input("Which keyword should be used? ")

encrypted_result = encrypt_text(text_input, keyword_input)
print(encrypted_result)
