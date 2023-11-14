"""Practicing Dictionaries!"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")

print(f"There are {ice_cream['chocolate']} orders of chocolate.")
ice_cream["vanilla"] = 10

print(f"There are {len(ice_cream)} total flavors!")

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("There are no orders of mint.")

print()

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")