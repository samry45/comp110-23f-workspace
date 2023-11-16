"""File to define River class."""
__author__ = "730642818"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Defining River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check the ages of Bear and Fish."""
        new_bears: list[Bear] = []            
        new_fish: list[Fish] = []
        for x in self.bears:
            testing_bear = x
            if testing_bear.age <= 5:
                new_bears.append(x)
        for x in self.fish:
            testing_fish = x
            if testing_fish.age <= 3:
                new_fish.append(x)
        self.bears = new_bears
        self.fish = new_fish
        return None

    def bears_eating(self):
        """Bears are eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Check hunger_score."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Increase Fish."""
        baby_fish: int = len(self.fish) // 2
        baby_fish *= 4
        idx: int = 0
        while idx < baby_fish:
            self.fish.append(Fish)
        return None
    
    def repopulate_bears(self):
        """Increase Bear."""
        baby_bears: int = len(self.bears) // 2
        idx: int = 0
        while idx < baby_bears:
            self.bears.append(Bear)
            idx += 1
        return None
    
    def view_river(self):
        """Show River conditions."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Go through seven days."""
        for x in range(7):
            self.one_river_day()
       
    def remove_fish(self, amount: int):
        """Remove the frontmost fish."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1