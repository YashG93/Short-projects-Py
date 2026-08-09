sentence=input('Enter sentence: ')
words=sentence.split()
word_fre={}
for word in words:
    word=word.strip(',.?').lower()
    if word in word_fre:
        word_fre[word]+=1
    else:
        word_fre[word]=1

print(word_fre)







