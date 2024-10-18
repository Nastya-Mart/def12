def single_root_words (root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word in i:
            same_words.append(i)
    return same_words
result = single_root_words('test', 'apple', 'hello', 'temp', 'galaxy', 'testing', 'test')
print(result)




single_root_words('test')





