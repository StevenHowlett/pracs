word_to_count = {}
user_text = input('text')
words = user_text.split()
longest_word_length = 0
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1
    if len(word) > longest_word_length:
        longest_word_length = len(word)
for word,count in sorted(word_to_count.items()):
    print("{:<{}} : {}".format(word,longest_word_length,count))
