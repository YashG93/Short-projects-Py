
def stutter_fun(input_word):
    if len(input_word)<2:
        return 'Word need at least two character long.'
    
    stutter_string=f'{input_word[:2]}...{input_word[:2]}...{input_word} '
    return stutter_string

word=input('Enter a word: ')
print(stutter_fun(word))