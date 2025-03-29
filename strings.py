"""Functions for creating, transforming, and adding prefixes to strings."""

# def add_prefix_un(word):
#     return "un" + word

# print(add_prefix_un("happy"))
# print(add_prefix_un("manageable"))

def make_word_groups(vocab_words):
    new_s = ''
    for w in vocab_words[1:-1]:
        new_s = new_s + (vocab_words[0] + '::' + w) + '::'
        print(new_s)

print(make_word_groups(['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete', 'echolalia', 'encoder', 'biography']))