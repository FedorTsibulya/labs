class Animal:
    __name = ""
    __age = ""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return self.get_str()


class Zebra(Animal):
    __species = ""

    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.__species = species

    def set_species(self, species):
        self.__species = species

    def get_species(self):
        return self.__species

    def get_str(self):
        return " ".join(["Name:", self.get_name(), "\n",
                        "Age:", self.get_age(), "\n",
                        "Species:", self.get_species(), "\n",
                        "------------------------------------------------\n"])


class Dolpine(Animal):
    __species = ""

    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.__species = species
    
    def set_species(self, species):
        self.__species = species
    
    def get_species(self):
        return self.__species        

    def get_str(self):
        return " ".join(["Name:", self.get_name(), "\n",
                        "Age:", self.get_age(), "\n",
                        "Species:", self.get_species(), "\n",
                        "------------------------------------------------\n"])


if __name__ == "__main__":
    zebra = Zebra("Huan", "4", "Equus grevyi")
    dolphine = Dolpine("Alejandro", "5", "Platanista gangetica")
    print(zebra.get_str())
    print(dolphine.get_str())