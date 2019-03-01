"""
this code implement an automated teller machine
"""

code = "1608"   # the secret code
money = 10000   # the amount of the money in the start


def print_menu():
    """
    this function will print the menu
    :return: None
    """
    print("1.   print balance")
    print("2.   cache withdrawal")
    print("3.   exchange secret code")
    print("4.   exit")


def print_balance():
    """
    this function will print the current amount of money
    :return: None
    """
    print("Your current balance: $" + str(money))


def menu_withdrawal():
    """
    this function will print the withdrawal menu
    :return: None
    """
    print("1.   $20")
    print("2.   $50")
    print("3.   any other amount")
    print("4.   back to menu")


def check_secret_code():
    """
    this function will ask the user what is the secret code
    and the function will check if the code he entered is correct
    :return: True - the user input is correct
                otherwise - False
    """
    global code
    secret_code = input("Please enter your secret code: ")
    if secret_code == code:
        return True
    else:
        print("wrong code")
        return False


def remove_from_money(amount):
    """
    this function remove amount of money from my total money
    :param amount: the amount of money to remove
    :return: None
    """
    global money
    if money - amount < 0:  # if you don't have enough money
        print("Sorry, you don't have enough money")
        return
    money -= amount


def cache_withdrawal():
    """
    this function will cache withdrawal
    :return:
    """
    menu_withdrawal()
    choice = input("Please enter your choice: ")
    choice = int(choice)
    if choice == 1:
        remove_from_money(20)
    elif choice == 2:
        remove_from_money(50)
    elif choice == 3:
        amount = input("Please enter the amount of the money do you want to withdrawal: ")
        amount = int(amount)
        remove_from_money(amount)


def exchange_secret_code():
    """
    this function will change the secret code
    :return: None
    """
    new_code = input("Please enter the new secret code: ")
    global code
    code = new_code


def main():
    """
    main function
    """
    while True:
        print_menu()
        user_input = input("Please enter what would you want to do: ")
        if user_input == "4":
            print("Thanks goodbye")
            break
        else:
            if check_secret_code():
                if user_input == "1":
                    print_balance()
                elif user_input == "2":
                    cache_withdrawal()
                elif user_input == "3":
                    exchange_secret_code()
            print()


if __name__ == "__main__":
    main()