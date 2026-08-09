sub=['I','You']
verbs=['Play','Love']
obj=['Hockey','Football']

sentence=[]

for subs in sub:
    for ver in verbs:
        for objs in obj:
            sen=f'{subs} {ver} {objs}'
            sentence.append(sen)

for sen in sentence:
    print(sen)