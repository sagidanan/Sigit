"""
Exercise 5
"""


def check_id(il_id):
    """
    this function will check if the Israeli id is right
    :param il_id: the id to check
    :return: True - the id is right
             Otherwise - False
    """
    mask = [1, 2, 1, 2, 1, 2, 1, 2]
    part = il_id[:-1]
    if len(il_id) != 9:
        raise OverflowError
    try:
        checksum = int(il_id[-1:])
    except ValueError:
        raise ValueError
    sum_id = 0
    for i in range(len(part)):
        try:
            mul = mask[i] * int(part[i])
            mul = int(mul)
        except ValueError:
            raise ValueError
        if mul > 9:  # if the number has 2 digits - sum the digit
            mul -= 9
        sum_id += mul
    return True if (10 - (sum_id % 10) == checksum) else False


def main():
    try:
        print(check_id("211863683"))
    except ValueError:
        print("Error - Id has to contain numbers only")
    except OverflowError:
        print("ID must to be 9 numbers")


if __name__ == "__main__":
    main()