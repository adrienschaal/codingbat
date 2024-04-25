def make_tags(tag, word):
    '''
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
    '''
    return '<' + tag + '>' + word + '</' + tag + '>'

print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay')) 