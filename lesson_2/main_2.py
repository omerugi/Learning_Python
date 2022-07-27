if __name__ == '__main__':
    print('''<<<<<<Comments in the code>>>>>>''')

    # This is a comment for a piece of code
    # We are using it to explain what a piece of code / variable does
    # Very important when working in a team!

    # the "TO DO" - this is a special comment that works like notes and reminders
    # to do: ?
    # TO DO: ??
    # TODO: need to fix login page!

    # Task - explain what is x
    # in this example x counting the number of times 5 was in the list/array.
    x = 0
    for i in [5, 6, 7, 11, 3, 5, 8]:
        if i == 5: x += 1


    def foo(age, name):
        """
        This will be an explanation of the function.
        ( does are explanation of the parameters of the function and what it returns)
        :param age: int that represents the users age
        :param name: str that represents the users name
        :return: str...
        """
        return f"My name is {name} and my age is {age}"


    '''
    This is a longer comment
    '''

    # Task - explain what the function above does, what are the parameter, and what is the return value.

    # Comments are also used to "mute" line of code
    y = 11
    print(y)
    y = y * 2 - 5
    print(y)

    print('''<<<<<< Variables Names >>>>>>''')
    # Always try to make the names logical!
    # Makes it easier to read the code

    # Types of naming formats
    myvar = "John"  # Could be hard to read - basic
    my_var = "John"  # Could be long - Snake Case
    _my_var = "John"  # Not useful all the times - For self vars
    myVar = "John"  # Could be hard to read BUT very common to use in short names - Camel Case
    MYVAR = "John"  # Using it usually only for setting variables
    myvar2 = "John"  # Numbering

    # Task - at the beginning we saw var 'x', what could be a more logical name?
    # Answer: counting_fives = 0

    print('''<<<<<< Try - Except >>>>>>''')
    # Few words about import
    import sys
    import traceback

    # # Non-specific errors
    # try:
    #     z
    # except:
    #     traceback.print_exc()
    #
    # try:
    #     print(banana)
    # except Exception as e:
    #     print(e.with_traceback(sys.exc_info()[2]))
    #
    # print("We made it all the way here!")
    #
    # # Specific errors
    # try:
    #     # _y = 1 / 0
    #     y = test
    # except ZeroDivisionError:
    #     print("div by zero")
    #     traceback.print_exc()
    # except:
    #     print("whatever")
    #     traceback.print_exc()
    #
    # print("We made it again!")
    #
    # # Custom errors
    #
    # try:
    #     x = 11
    #     if type(x) != str:
    #         raise Exception("The variables type was wrong")
    # except:
    #     traceback.print_exc()
    #
    # try:
    #     x = 11 / 0
    # except:
    #     print(Exception("The variables type was wrong "))

    # print('''<<<<<< Types & Typing >>>>>>''')
    # _string = "Hey!"  # Store text
    # _num = 1  # Store natural numbers
    # _flo = 1.2  # Store numbers with decimal point
    # _boole = True or False  # Store true / false
    #
    # # To make variable clearer we can use typing:
    # string: str = "Hey!"  # Store text
    # num: int = 1  # Store natural numbers
    # flo: float = 1.2  # Store numbers with decimal point
    # boole: bool = True or False  # Store true / false
    #
    # # NoneType
    # none = None  # This an empty var

    # # Many Values to Multiple Variables
    # i, j, q = "Orange", "Banana", "Cherry"
    # print(i, j, q)
    #
    # # One Value to Multiple Variables
    # s = w = v = "Orange"
    # print(s, w, v)
    #
    print('''<<<<<< Types Functions >>>>>>''')
    # We can add together same types of vars
    x: int = 3
    y: int = 5
    print(x + y)
    x: float = 3.0
    y: float = 5.0
    print(x + y)
    x, y = "hello", "world"
    print(x + y)
    # Not allowed to add of different "types" but there are exceptions
    x: float = 3.0
    y: int = 5
    print(x + y)


    '''
    TODO: Task - Make a "try except" block with two var of different types,
    adds them together an print the error to the terminal.
    '''
    name: str = "omer"
    age: int = 20
    try:
        y=8
        name="yoav"
        y+name
    except:
        print("impossible to connect y+name")

