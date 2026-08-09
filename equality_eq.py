
def signs(expre):
    try :
        return eval(expre)
    except:
        return False

print(signs('3<7<11'))