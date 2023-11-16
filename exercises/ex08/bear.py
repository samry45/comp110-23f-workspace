"""File to define Bear class."""


class Bear:
    """Defining Bear class."""

    age: int
    hunger_score: int

    def __init__(self, bear_age: int = 0, bear_hunger_score: int = 0):
        """Constructor."""
        self.age = bear_age
        self.hunger_score = bear_hunger_score
        return None

    def one_day(self):
        """Adding one to age and hunger_score."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increasing hunger_score."""
        self.hunger_score += num_fish
        return None