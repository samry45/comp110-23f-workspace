"""File to define Fish class."""


class Fish:
    """Defining Fish class."""

    age: int
    
    def __init__(self, fish_age: int = 0):
        """Constructor."""
        self.age = fish_age
        return None
        
    def one_day(self):
        """Increasing age by one."""
        self.age += 1
