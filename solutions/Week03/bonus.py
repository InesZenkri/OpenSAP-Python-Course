while True:
    shift = input("Please enter the number of places to shift: ")
    if shift.isdecimal() and 0 <= int(shift) <= 25:
        shift = int(shift)
        break
    else:
        print("You need to enter a number between 0 and 25!")

sentence = input("Please enter a sentence: ").lower()
sentence = sentence.lower()
encrypted_sentence = ''
for char in sentence:
    if char.isalpha():
        encrypted_sentence += chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) 
    else:
        encrypted_sentence += char
print("The encrypted sentence is: ",encrypted_sentence)
