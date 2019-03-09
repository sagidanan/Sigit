"""
Exercise 6
"""


def Map(func, params):
    """
    this function implements the map function
    :param func: a pointer to the function
    :param params: a list of params that will send to the function
    :return: a new list with results of the function on each param
    """
    # list comprehension - of each param add to the list the result from the function
    return [func(param) for param in params]


def square(value):
    """
    this function will return the square of a value
    :param value: the value to square
    :return: the result
    """
    return value ** 2   # same as value ^ 2 (not xor)


def main():
    """
    main function
    """
    params = [x for x in range(1, 21)]  # get a list with values 1 to 20 = [1, 2, 3, 4, ... , 20]
    print(Map(square, params))  # ran map function with the function square and params


if __name__ == "__main__":
    main()