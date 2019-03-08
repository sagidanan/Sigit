"""
Exercise 4
"""


def compress(string):
    """
    this function will compress a string
    :param string: the string to compress
    :return: the compressed string
    """
    compressed = ""
    count = 1
    compressed += string[0]
    for i in range(len(string) - 1):  # goes until before the last value
        if string[i] == string[i + 1]:
            count += 1
        else:
            compressed += str(count)
            compressed += string[i + 1]  # add the new letter
            count = 1
    compressed += str(count)  # add the count of the last letter
    return compressed


def main():
    """
    main function
    """
    string = "aabbbbcdddeaaaaa" # string to compress
    print("string = ", string)
    print("compressed string = ", compress(string))


if __name__ == "__main__":
    main()