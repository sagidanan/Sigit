"""
this code implement an automated teller machine
"""


class ATM:
    def __init__(self, code, init_money=10000):
        self._code = code                   # the secret code
        self._money = init_money       # the amount of the money in the start

    @staticmethod
    def user_input(start, end):
        """
        this function will get an input from the user in some range(from x to y)
        :param start: the 'from' of the input
        :param end: the 'to' of the input
        :return: the user input
        """
        while True:
            data = input("Please enter what would you want to do: ")
            try:
                data = int(data)    # if the user input is letter - exception will thrown
                if data < start or data > end:
                    print("Error!! please enter a number between " + str(start) + " to " + str(end))
                else:
                    return data
            except ValueError:
                print("Error!! please enter a number between " + str(start) + " to " + str(end))

    def check_secret_code(self):
        """
        this function will ask the user what is the secret code
        and the function will check if the code he entered is correct
        :return: True - the user input is correct
                    otherwise - False
        """
        secret_code = input("Please enter your secret code: ")
        if secret_code == self._code:
            return True
        else:
            print("wrong code")
            return False

    @staticmethod
    def print_menu():
        """
        this function will print the menu
        :return: None
        """
        print("1.   print balance")
        print("2.   cache withdrawal")
        print("3.   exchange secret code")
        print("4.   exit")

    def print_balance(self):
        """
        this function will print the current amount of money
        :return: None
        """
        print("Your current balance: $" + str(self._money))

    @staticmethod
    def menu_withdrawal():
        """
        this function will print the withdrawal menu
        :return: None
        """
        print("1.   $20")
        print("2.   $50")
        print("3.   any other amount")
        print("4.   back to menu")

    def remove_from_money(self, amount):
        """
        this function remove amount of money from my total money
        :param amount: the amount of money to remove
        :return: None
        """
        if self._money - amount < 0:  # if you don't have enough money
            print("Sorry, you don't have enough money")
            return
        self._money -= amount

    def cache_withdrawal(self):
        """
        this function will cache withdrawal
        :return:
        """
        self.menu_withdrawal()
        choice = self.user_input(1, 4)
        if choice == 1:
            self.remove_from_money(20)
        elif choice == 2:
            self.remove_from_money(50)
        elif choice == 3:
            try:
                amount = input("Please enter the amount of the money do you want to withdrawal: ")
                amount = int(amount)
                self.remove_from_money(amount)
            except ValueError:
                print("Error input!!")

    def exchange_secret_code(self):
        """
        this function will change the secret code
        :return: None
        """
        try:
            new_code = input("Please enter the new secret code: ")
            int(new_code)   # if it will throw exception its mean that the user input isn't contain only numbers
            self._code = new_code
        except ValueError:
            print("code needs to be contain only numbers")

    def start(self):
        while True:
            self.print_menu()
            data = self.user_input(1, 4)
            if data == 4:
                print("Thanks goodbye")
                break
            else:
                if self.check_secret_code():
                    if data == 1:
                        self.print_balance()
                    elif data == 2:
                        self.cache_withdrawal()
                    elif data == 3:
                        self.exchange_secret_code()
                print()


def main():
    """
    main function
    """
    my_atm = ATM("1608", 15000)
    my_atm.start()


if __name__ == "__main__":
    main()