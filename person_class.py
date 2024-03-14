class person:   # A class called person
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")
        
# Here, I created aninstance of the person class
person = person("Chibuzor", 27, "male")

#Call the introduce method 

person.introduce()