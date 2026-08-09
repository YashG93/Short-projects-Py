from collections import OrderedDict

def check_dict(input_string,ref_string):
    new_string=OrderedDict.fromkeys(input_string)
    refference=OrderedDict.fromkeys(ref_string)

    return new_string==refference

my_string='Hello world'
refer='Helo wrd'
if check_dict(my_string,refer):
    print('Your string matches  refference string.')

else:
    print('Your string not matched to refference string.')