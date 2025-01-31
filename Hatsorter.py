import random

class Hat:
    houses = ["G","H","R","S"]

    @classmethod
    def sort(cls,name):
        print(f"{name} is in {random.choice(cls.houses)}")

def main():
    Hat.sort("Harry")
    print(Hat.houses)

main()