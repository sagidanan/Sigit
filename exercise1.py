"""
this code implement an automated teller machine (ATM)
"""


class ATM:
    def __init__(self, code, init_money=10000):
        self._code = code                   # the PIN code
        self._money = init_money            # the amount of the money in the start
        # this method implements a strategy design pattern
        self._menu_strategy = {1 : self.print_balance, 2 : self.cash_withdrawal, 3 : self.exchange_PIN_code}

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
                    raise
                else:
                    return data
            except ValueError:
                print("Error!! please enter a number between " + str(start) + " to " + str(end))

    def check_PIN_code(self):
        """
        this function will ask the user what is the PIN code
        and the function will check if the code he entered is correct
        :return: True - the user input is correct
                    otherwise - False
        """
        PIN_code = input("Please enter your PIN code: ")
        if PIN_code == self._code:
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
        print("2.   cash withdrawal")
        print("3.   exchange PIN code")
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
        print("Please take your money :)")

    @staticmethod
    def money_withdrawal_validation(amount):
        """
        this function will check if amount of money is valid to withdrawal
        validation:     if the amount is divided with 20 or 50 or both without a remainder
        :param amount: the amount of money
        :return: True if the amount is valid, otherwise - False
        """
        return True if (amount % 50) % 20 == 0 else False

    def cash_withdrawal(self):
        """
        this function will cash withdrawal
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
                if self.money_withdrawal_validation(amount):
                    self.remove_from_money(amount)
                else:
                    print("Not a valid amount")
            except ValueError:
                print("Error input!!")

    def exchange_PIN_code(self):
        """
        this function will change the PIN code
        :return: None
        """
        try:
            new_code = input("Please enter the new PIN code: ")
            int(new_code)   # if it will throw exception its mean that the user input isn't contain only numbers
            self._code = new_code
            print("PIN code changed")
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
                if self.check_PIN_code():
                    self._menu_strategy[data]()     # call the function by user-input (strategy design pattern)
                print()


def main():
    """
    main function
    """
    my_atm = ATM("1608", 15000)
    my_atm.start()


if __name__ == "__main__":
    main()