def word_length(text):
    total = len(text.split())
    print('words: {}'.format(total))
    for num, word in enumerate(text.split(), 1):
        yield '{}/{}: {}'.format(num, total, len(word))


text = 'a quick brown fox jumped over the lazy dog'
wl = word_length(text)

for word in wl:
    print(word)

