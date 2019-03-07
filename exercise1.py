"""
this code implement an automated teller machine (ATM)
"""


class ATM:
    def __init__(self):
        self._accounts = {}             # the dictionery who saves all the accounts:
                                        # {key=PIN_CODE : value=CURRENT_MONEY}

        # this method implements a strategy design pattern
        self._menu_strategy = {1: self.print_balance, 2: self.cash_withdrawal, 3: self.exchange_PIN_code}

    def add_account(self, PIN, init_money):
        """
        this function will add a new PIN code to the dictionary
        :param PIN: the pin code
        :param init_money: the initialize money
        :return: None
        """
        if PIN in self._accounts:
            print("Account already exist")
        else:
            self._accounts[PIN] = init_money

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
                    raise ValueError   # throw exception - go to line: except ValueError
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
        if PIN_code in self._accounts:
            return PIN_code
        else:
            print("wrong code")
            return ""

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

    def print_balance(self, PIN):
        """
        this function will print the current amount of money
        :param: PIN: the PIN code
        :return: None
        """
        print("Your current balance: $" + str(self._accounts[PIN]))

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

    def remove_from_money(self, PIN, amount):
        """
        this function remove amount of money from my total money
        :param amount: the amount of money to remove
        :param: PIN: the PIN code
        :return: None
        """
        if self._accounts[PIN] - amount < 0:  # if you don't have enough money
            print("Sorry, you don't have enough money")
            return
        self._accounts[PIN] -= amount
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

    def cash_withdrawal(self, PIN):
        """
        this function will cash withdrawal
        :param: PIN: the PIN code
        :return:
        """
        self.menu_withdrawal()
        choice = self.user_input(1, 4)
        if choice == 1:
            self.remove_from_money(PIN, 20)
        elif choice == 2:
            self.remove_from_money(PIN, 50)
        elif choice == 3:
            try:
                amount = input("Please enter the amount of the money do you want to withdrawal: ")
                amount = int(amount)
                if self.money_withdrawal_validation(amount):
                    self.remove_from_money(PIN, amount)
                else:
                    print("Not a valid amount")
            except ValueError:
                print("Error input!!")

    def exchange_PIN_code(self, PIN):
        """
        this function will change the PIN code
        :param: PIN: the PIN code
        :return: None
        """
        try:
            new_code = input("Please enter the new PIN code: ")
            int(new_code)   # if it will throw exception its mean that the user input isn't contain only numbers
            if new_code not in self._accounts:
                self._accounts[new_code] = self._accounts.pop(PIN)
                print("PIN code changed")
            else:
                print("ERROR: new PIN code already exist")
        except ValueError:
            print("code needs to be contain only numbers")

    def start(self):
        """
        this function will play the ATM
        it will show a menu to a user and he will need to choose what to do
        :return: None
        """
        while True:
            self.print_menu()
            data = self.user_input(1, 4)
            if data == 4:
                print("Thanks goodbye")
                break
            else:
                PIN = self.check_PIN_code()
                if PIN != "":
                    self._menu_strategy[data](PIN)     # call the function by user-input (strategy design pattern)
                print()


def main():
    """
    main function
    """
    my_atm = ATM()
    # add all the accounts
    my_atm.add_account("4608", 10000)
    my_atm.add_account("1234", 15000)
    my_atm.add_account("1593", 4000)
    # play the ATM
    my_atm.start()


if __name__ == "__main__":
    main()