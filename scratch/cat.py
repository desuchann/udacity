"""How to catto."""

class Cat():
    """This creates a catto."""
    
    def __init__(self, name:str, age:int, isIndoor=True):
        """Initialise cattto..."""
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def __repr__(self):
        return f"{self.name!r}, {self.age}"

    def speak(self) -> None:
        """Make a cute cat sound.

        >>> kitty.speak()
        Spot says, purrrrrr."""
        print(f'{self.name} says, purrrrrr.')
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'kitty': Cat('Spot', 3, False)})