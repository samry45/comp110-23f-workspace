"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730642818"


class Simpy:
    """Simpy Class Definition."""

    values: list[float]

    def __init__(self, numbers: list[float]):
        """Constructor."""
        self.values = numbers

    def __str__(self) -> str:
        """Represent Simpy as a string."""
        string: str = f"Simpy({self.values})"
        return string
    
    def __add__(self, adding: Union[Simpy, float]) -> Simpy:
        """Add Simpys and floats together."""
        new_values: list[float] = []
        if type(adding) is Simpy:
            assert len(self.values) == len(adding.values)
            idx: int = 0
            while idx < len(self.values):
                new_values.append(self.values[idx] + adding.values[idx])
                idx += 1
        if type(adding) is float:
            for num in self.values:
                new_values.append(num + adding)
        new_Simpy: Simpy = Simpy(new_values)
        return new_Simpy
    
    def __pow__(self, power: Union[Simpy, float]) -> Simpy:
        """Raise one Simpy to the power of another or a float."""
        new_values: list[float] = []
        if type(power) is Simpy:
            assert len(self.values) == len(power.values)
            idx: int = 0
            while idx < len(self.values):
                result: float = self.values[idx] ** power.values[idx]
                new_values.append(result)
                idx += 1
        if type(power) is float:
            for num in self.values:
                new_values.append(num ** power)
        new_Simpy: Simpy = Simpy(new_values)
        return new_Simpy
    
    def __eq__(self, checking: Union[Simpy, float]) -> list[bool]:
        """Check to see it the lists/floats match."""
        output_list: list[bool] = []
        if type(checking) is Simpy:
            assert len(self.values) == len(checking.values)
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] == checking.values[idx]:
                    output_list.append(True)
                else: 
                    output_list.append(False)
                idx += 1
        if type(checking) is float:
            for num in self.values:
                if num == checking:
                    output_list.append(True)
                else: 
                    output_list.append(False)
        return output_list
    
    def __gt__(self, checking: Union[Simpy, float]) -> list[bool]:
        """Check to see it the lists/floats match."""
        output_list: list[bool] = []
        if type(checking) is Simpy:
            assert len(self.values) == len(checking.values)
            idx: int = 0
            while idx < len(self.values):
                if self.values[idx] > checking.values[idx]:
                    output_list.append(True)
                else: 
                    output_list.append(False)
                idx += 1
        if type(checking) is float:
            for num in self.values:
                if num > checking:
                    output_list.append(True)
                else: 
                    output_list.append(False)
        return output_list
    
    def __getitem__(self, index: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Call specific item or Simpy."""
        if type(index) is int:
            item: float = self.values[index]
            return item
        if type(index) is list[bool]:
            assert len(self.values) == len(index)
            true_values = list[float] = []
            idx: int = 0
            while idx < len(self.values):
                if index[idx] is True:
                    true_values.append(self.values[idx])
                idx += 1
            result: Simpy = Simpy(true_values)
            return result
    
    def fill(self, filler: float, amount: int) -> None:
        """Fill in the list with a set of repeating floats."""
        new_list: list[float] = []
        for x in range(0, amount):
            new_list.append(filler)
        self.values = new_list
        return None

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the list with a set of increasing/decreasing numbers."""
        assert step != 0.0
        num: float = start
        new_list: list[float] = []
        if step > 0.0:
            while num < stop:
                new_list.append(num)
                num += step
        else: 
            while num > stop:
                new_list.append(num)
                num += step
        self.values = new_list
        return None

    def sum(self) -> float:
        """Add all values in the list."""
        total: float = 0.0
        for num in self.values:
            total += num
        return total
    