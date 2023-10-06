name: str = input("Name? ")

if len(name)>6:
    print("Do you have a nickname?")
elif name == "Alyssa":
        print("I love Comp110!")
else:
        print("Nice to meet you, " + name)