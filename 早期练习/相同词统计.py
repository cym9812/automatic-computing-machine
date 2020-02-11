def word_count(speech):
    word_count_dict = {}
    word_list = speech.split()
    for word in word_list:
        word_count_dict[word] = word_list.count(word)
    return word_count_dict
