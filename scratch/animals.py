"""Playing around with inheritance and instantiation via classmethods."""


class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        """Hear the animal!"""
        print(f'{self.name} says, "{self.sound}"')

    @classmethod
    def spawn(cls, name: str, mother: object, father: object):
        breed = mother.breed
        if mother.breed != father.breed:
            breed = f'{mother.breed}-{father.breed} Mix'
        weight = (mother.weight + father.weight)/(2*10)
        return cls(name, 0, breed, weight, 'woof')


class Cat(Animal):
    isIndoor = False

    def __init__(self, name, age, sound, isIndoor=True):
        """Create a new cat"""
        self.isIndoor = isIndoor
        super().__init__(name, age, sound)


class Frog(Animal):
    def __init__(self, name, age, sound, colour):
        self.colour = colour
        super().__init__(name, age, sound)


class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str, weight: int, sound: str):
        self.breed = breed
        self.weight = weight
        super().__init__(name, age, sound)


if __name__ == "__main__":
    wiskers = Cat('Wiskers', 3, 'purr')
    paws = Dog('Mr. Paws', 4, 'dachshund', 18, 'woof')
    prince = Frog('Prince', 1, 'ribbit', 'spotty')
    wiskers.speak()
    paws.speak()
    prince.speak()

    sally = Dog('Sally', 6, 'chihuahua', 7, 'woof')
    henry = Dog('Henry', 7, 'terrier', 15, 'woof')
    trixy = Dog.spawn('Trixy', sally, henry)
    print(trixy.breed)