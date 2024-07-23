## Inheritance practiceee

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale,Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swin(self):
        print("moving in water")

    def breath(self):
        super().breath()
        print("doing this underwater")## Overwrite a class

nemo = Fish()
nemo.swin()
nemo.breath()
print(nemo.num_eyes)