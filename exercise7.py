"""
Exercise 7
"""
import timeit


def memoize(func):
    """
    this is the outer function - initialize the cache decorator
    :param func: the pointer to the function
    :return: the inner function - that made the decorator (memoization)
    """
    cache = {}  # initialize the dictionary that saves the results - {KEY=args: VALUE=the result from func}

    # inner function
    def memoize_func(*args):    # *args - can be more then one argument (presented as one object)
        """
        this is the inner function, it implement the cache decorator, insert value and call the function if needed
        this function wrap func - every time we will call func, the code will call to this inner function
        :param args: the argument to enter to func
        :return: the result func
        """
        if args in cache:   # if the arguments in the dictionary - return the value
            return cache[args]
        result = func(*args)    # otherwise call the function and add the result to the dictionary
        cache[args] = result
        return result

    return memoize_func  # return the inner function


# @memoize same as write: get_count_prime = memoize(get_count_prime)
# every time we will call get_count_prime is like to call to memoize_func (because memoize return this function)
@memoize
def get_count_prime(start, stop):
    """
    this function return the amount prime numbers from start to stop
    :param start: from number
    :param stop: to number
    :return: the amount of prime numbers
    """
    count = 0
    for possible_prime in range(start, stop + 1):
        is_prime = True
        for num in range(2, possible_prime):
            if possible_prime % num == 0:
                is_prime = False
        if is_prime:
            count += 1
    return count


def main():
    """
    main function
    """
    # get the amount of prime numbers between 20 to 10000
    # this line may take a long time
    print("there is ", get_count_prime(20, 10000), " prime numbers between 20 to 10000")
    # this line will shown exactly after the above line
    print("there is ", get_count_prime(20, 10000), " prime numbers between 20 to 10000")


if __name__ == "__main__":
    main()