
class Person:
    def getgender(self):
        return 'Unknown'
    
class Male(Person):
    def getgender(self):
        return 'Male'
    
class Female(Person):
    def getgender(self):
        return 'Female'
    
person=Person()
male=Male()
female=Female()

print(person.getgender())
print(male.getgender())
print(female.getgender())