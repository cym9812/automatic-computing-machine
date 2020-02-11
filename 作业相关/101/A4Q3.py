def get_keywords_occurrences(filename):
    keywords_list = {"and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "False", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "print", "raise", "return", "True", "try", "while", "with", "yield"}
    word_count_dict = {}
    file = open(filename, "r")
    words = file.read()
    file.close()
    word_list = words.split()
    for word in word_list:
        if word in keywords_list:
            word_count_dict[word] = word_list.count(word)
    return word_count_dict
