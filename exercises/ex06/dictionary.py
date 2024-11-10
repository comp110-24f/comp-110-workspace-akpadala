"""practice with dictionary functions in exercise 6!"""

__author__ = "730745996"


def invert(orig_dict: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    # we will need to create a new empty dictionary in which the keys and values will
    # be switched and added to as we need to cross check the keys (current values) when
    # switched to make sure there are no duplicates. and if the original dictionary is
    # getting mutated, this will not be possible
    for key in orig_dict:
        value: str = orig_dict[key]
        duplicate: bool = False
        # we are initially setting duplicate equal to flase as we don't know if there
        # are any duplicates. this is only for the case of initializing the variable
        for orig_key in new_dict:
            if orig_key == value:
                duplicate = True
                break
                # this checks to see if each key in the new dictionary (value in
                # original dictionary) equals that of another value and if it does,
                # duplicate is now set to true as it shows there is a duplicate when
                # inversed and a keyerror needs to be raised. we then have to include a
                # break as we only need one instance of a duplicate to indicate that
                # there will be a key issue.
        if duplicate:
            raise KeyError(f"Duplicate key detected when inverting: {value}")
        new_dict[value] = key
        # after checking for an error, this now intializes each value as a key in the
        # new dictionary and contiues to return the final new dictionary
    return new_dict


def favorite_color(dict_one: dict[str, str]) -> str:
    color_count: dict[str, int] = {}
    first_occurance: dict[str, int] = {}
    index: int = 0
    for name in dict_one:
        color = dict_one[name]
        # gets favorite color for the current name and then checks to see if color is
        # already counted in the color_count dict
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
            first_occurance[color] = index
        index += 1
        # moves to the next index
    most_pop_color: str = ""
    # will store the most popular color which is what we are trying to get, at the end
    # we will return this variable
    max_count: int = 0
    for color in color_count:
        count: int = color_count[color]
        if count > max_count or (
            count == max_count
            and first_occurance[color] < first_occurance[most_pop_color]
            # accounts for two or more popular colors (a tie), if so it checks which
            # one is the first occurance
        ):
            most_pop_color = color
            max_count = count
    return most_pop_color


def count(vals: list[str]) -> dict[str, int]:
    final: dict[str, int] = {}
    for val in vals:
        if val in final:
            # checks to see if the item is already a key and if it is the count
            # increases
            final[val] += 1
        else:
            # if not, it means that it is a new occurance and therefore needs to get
            # added to a dictionary with a new count starting
            final[val] = 1
    return final


def alphabetizer(vals: list[str]) -> dict[str, list[str]]:
    final_dict: dict[str, list[str]] = {}
    for val in vals:
        first_letter = val[0].lower()
        # .lower was given in the instructions. it converts the first letter of the
        # word to lowercase
        if first_letter in final_dict:
            final_dict[first_letter].append(val)
            # if the letter oes not exist, this intializes the list for the letter
        else:
            final_dict[first_letter] = [val]
    return final_dict


def update_attendance(dict_comb: dict[str, list[str]], day: str, student: str) -> None:
    if day in dict_comb:
        # this checks to see if the day already exists in the dictionary, if it does
        # the student will get added to the list
        if student not in dict_comb[day]:
            dict_comb[day].append(student)
    else:
        # if not, a new list with the student will be created
        dict_comb[day] = [student]
