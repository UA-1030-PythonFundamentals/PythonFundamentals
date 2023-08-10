##Task2. Create a class Human, everyone has a name, create a method in the
##class that displays a welcome message to each person. Create a class method
##in the class that returns information that it is a species of "Homosapiens". And
##in the class create a static method that returns an arbitrary message.
##--HW10-- PT19-- July 19, 2023. 

class Human:

    def __init__(self,name,spieces):
        self.name = name
        self.spieces = spieces

    def __str__(self):
        return f"This is a {self.spieces} named {self.name}."
        
    def greets(self):
<<<<<<< HEAD
        return f"Hello {self.name}!"

    def message(self):
=======
        
        return f"Hello {self.name}!"

    def message(self):
        
>>>>>>> 2d83f7cab5da9ae1700507787c46da8d9e41028b
        return f"How are you doing {self.name.upper()}?"
        

#####################----------Checking--------#######################

f = Human("John","man")
print(f);print()
f.greets();print()
f.message();print()

#VN
