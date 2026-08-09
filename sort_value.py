sample_dict={'apple':1,'banana':2,'Kevi':3}
sorted_keys=dict(sorted(sample_dict.items()))

for key,value in sorted_keys.items():
    print(f'{key}:{value}')