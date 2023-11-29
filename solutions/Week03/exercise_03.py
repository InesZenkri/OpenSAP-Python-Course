sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
encrypted_sentence = ''
for char in sentence:
    if char.isalpha():
        encrypted_sentence += chr(((ord(char) - ord('a') + 5) % 26) + ord('a')) 
    else:
        encrypted_sentence += char
print("The encrypted sentence is: ",encrypted_sentence)