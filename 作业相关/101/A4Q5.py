def words_to_morse(morse_dict, words):
    result = []
    words = words.replace(" ", "")
    for letter in words:
        letter = letter.upper()
        result.append(morse_dict[letter])
    return result


morse_dict = {'8': '---..', '3': '...--', 'H': '....', 'E': '.', ';': '-.-.-.', '=': '-...-', '7': '--...', '0': '---...'}
print(words_to_morse(morse_dict, 'hello'))
