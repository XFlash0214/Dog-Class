class Dog :
    name="Buddy"
    color="brown"
    def Bark(self):
        print("Woof!  My Name is " + self.name)

mydog=Dog()
mydog.name="Mila"
print(mydog.name)

nextdog=Dog()
nextdog.name="Snickers"

mydog.Bark()
nextdog.Bark()
