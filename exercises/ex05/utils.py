"""program where I implement list utility functions"""

__author__ = "730745996"


def only_evens(vals: list[int]) -> list[int]:
    end_list = []  # need an empty list to append values to
    for val in vals:
        if val % 2 == 0:
            # modulus function is used to indicate if something is even. if it is
            # divisble by 2 then there will be a remainder of 0
            end_list.append(val)
    return end_list


def sub(vals: list[int], start_index: int, end_index: int) -> list[int]:
    end_list = []
    if start_index < 0:
        start_index = 0
    if end_index > len(vals):
        end_index = len(vals)
        # above indicate the two "invalid" cases (negative start index or out of bounds
        # end index) where we would need to set our own index
    if start_index >= end_index or len(vals) == 0:
        return end_list
        # need to return an empty list because the start index being greater than the
        # end index or the length of the list being 0 indictes it is an empty list
        # if not all the cases listed above, then we can go ahead an append the values
        # from start index and end index into a new list which is what is happening in
        # the function underneath
    for i in range(start_index, end_index):
        end_list.append(vals[i])
    return end_list


def add_at_index(vals: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(vals):
        raise IndexError("Index is out of bounds for the input list")
    vals.append(0)
    # the 0 has to be added as we are not removing any integers from the list and
    # therefore need to make space for the new element being added in
    for i in range(len(vals) - 1, index, -1):
        vals[i] = vals[i - 1]
        # this function goes backwards in the range of the list and pushes everything
        # one place to the right so that the element can fit at the indicated index
    vals[index] = element
