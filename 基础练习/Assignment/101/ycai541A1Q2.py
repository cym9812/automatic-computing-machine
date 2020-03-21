"""
Name: Yimeng Cai
username: ycai541
ID number: 455251836
Description: Calculates the surface area and volume of a right regular octagonal prism
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
scrambled_alphabet = "updvcslymkxzfrejnaowhgbqit"
print("#" * 20)
print("#A Simple Encrypter#")
print("#" * 20)
print()
print("alphabet: ", alphabet, sep="")
print("scrambled_alphabet: ", scrambled_alphabet, sep="")
print()
original_word = input("Please enter a 5 letter word: ")
letter_one = original_word[0]
position_one = scrambled_alphabet.find(letter_one)
encrypted_letter_one = alphabet[position_one]
letter_two = original_word[1]
position_two = scrambled_alphabet.find(letter_two)
encrypted_letter_two = alphabet[position_two]
letter_three = original_word[2]
position_three = scrambled_alphabet.find(letter_three)
encrypted_letter_three = alphabet[position_three]
letter_four = original_word[3]
position_four = scrambled_alphabet.find(letter_four)
encrypted_letter_four = alphabet[position_four]
letter_five = original_word[4]
position_five = scrambled_alphabet.find(letter_five)
encrypted_letter_five = alphabet[position_five]
encrypted_word = encrypted_letter_one + encrypted_letter_two + encrypted_letter_three +\
                 encrypted_letter_four + encrypted_letter_five
print("Encrypted word: ", encrypted_word, sep="")
