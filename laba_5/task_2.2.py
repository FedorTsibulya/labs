class Mother():
    age = 0
    
    def __init__(self, age):
        self.age = age
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
    
    
    
class Daughter(Mother):
    def set_age(self, age_daughter):
        self.age = age_daughter
        
        
if __name__ == "__main__":
    mother = Mother(46)
    daughter = Daughter(24)
    daughter.set_age(13)
    print(mother.get_age(), daughter.get_age())