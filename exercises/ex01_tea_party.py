"""this program will help calculate the number of tea bags needed for a tea party dependent on the number of guests"""

_author_: str = "730745996"


def main_planner(guests: int) -> None:
    """This is the main function that brings all our functions together and produces a printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """This function defines and initializes the function tea bags which takes in the amount of people attending the tea party as a parameter. This parameter can be used when calling the function later on using an argument."""
    return people * 2


def treats(people: int) -> int:
    """This function calculates how many treats each person at the tea party will have based on how many people are there"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function will compute the vost of the tea bags and treats combined based on how many people are present at the tea party"""
    return (tea_count * 0.50) + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
"""this needs to go at the very bottom for the program to be able to run in trailhead"""
