"""
Exercise 2
"""


def calculate_list(list_to_sum):
    """
    this function will sum the list
    :param list_to_sum: the list - contain int only
    :return: the sum of the list
    """
    return sum(list_to_sum)


def option_a():
    """
    this function implement the first option
    the user enter number ofter number (until he enters 'stop') and then it will sum all his inputs and print it
    :return: None
    """
    num_list = []
    while True:
        num = input("Please enter a number to add to the list ('stop' to stop): ")
        if num.lower() == "stop":
            break
        try:
            num = int(num)  # convert the input to integer
            num_list.append(num)  # add his input to the list
        except ValueError:
            print("Must to be a number or 'stop'!!!")

    print("the sum is: ", calculate_list(num_list))  # sum the list


def option_b():
    """
    this function implement the second option
    the user enter the list like '1,2,3,4' and then we will sum the list and print the result
    :return: None
    """
    str_list = input("Please enter the list - split with ',' : ")
    num_list = str_list.split(",") # split the string by ',' and convert it to list
    try:
        num_list = [int(x) for x in num_list]   # for each value in the list
                                                # we will convert it to a number (from string)
        print("the sum is: ", calculate_list(num_list))
    except ValueError:
        print("list must contain only numbers and ',' !!")


def main():
    """
    the main function
    """
    strategy = {1: option_a, 2: option_b}
    print("This program sum the list!")
    while True:
        print("\n1. option a")
        print("2. option b")
        print("3. exit")
        choice = input("Please enter what would you like to do: ")
        try:
            choice = int(choice)    # convert the input to integer
        except ValueError:
            print("Please enter a number!")
            continue
        if choice < 1 or choice > 3:
            print("number must be between 1 - 3")
            continue
        if choice == 3:
            print("Thanks Bye")
            break
        strategy[choice]()  # call to the function by the choice - used strategy design pattern


if __name__ == "__main__":
    main()
