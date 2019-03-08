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
    checksum = int(il_id[-1:])
    sum_id = 0
    for i in range(len(part)):
        mul = mask[i] * int(part[i])
        mul = int(mul)
        if mul > 9:  # if the number has 2 digits - sum the digit
            mul -= 9
        sum_id += mul
    return True if (10 - (sum_id % 10) == checksum) else False


def main():
    print(check_id("211863683"))


if __name__ == "__main__":
    main()