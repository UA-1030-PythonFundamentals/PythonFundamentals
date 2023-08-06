# try:
#
#     print(8/0)
# except:
#     pass
# print("test")
# 6 + value * 2

# a = [5, 6, 7, 8]
# try:
#     print("Second element = {}".format(a[1]))
#     # Throws error since there are only 4 elements in array
#     # 0/0
#     print("Fifth element = {}".format(a[4]))
# except IndexError as e:
#     print(e)


# def is_even(number):
#     return number % 2 == 0
#
#
# try:
#     user_input = int(input("Enter an integer: "))
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")
# else:
#     if is_even(user_input):
#         print(f"{user_input} is even.")
#     else:
#         print(f"{user_input} is odd.")


# Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a / (a - 3)  # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b)  # throws NameError
#     # note that braces () are necessary here for multiple exceptions
# except ValueError as e:
#     print("Value Error!", e)
# except (NameError, ValueError):
#     print("NameError! NameError")
# except ZeroDivisionError:
#     print("ZeroDivisionError!")
# except:
#     print("Error!")
#
# try:
#     a = int(input("Enter your number: "))
#     print(7 / a)
#
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError as e:
#     print("ArithmeticError", e)
# except Exception as e:
#     print(e)

# try:
#     f = open("newfile.txt")
#     f.write("Second element: ")
# except:
#     print("Something went wrong when writing to the file")
# else:
#     print("Nothing went wrong")
# finally:
#     f.close()
#     print("The 'try except' is finished")
# def f():
#     try:
#         return 5
#     except:
#         pass
#     finally:
#         print("return 15")
#
#
# print(f())
# a = input("Enter your number: ")
# a, b = a.split(",")
# print(a, b)

# num = input('Numbers: ')
# num_1, num_2 = num.split(',')
# try:
#     print(int(num_1.strip()) / int(num_2.strip()))
# except ZeroDivisionError:
#     print('Zero!')
# except SyntaxError:
#     print('Syntax')
# except Exception:
#     print('Exceptions')
#
#
# try:
#     input_str = input("Enter two numbers separated by a comma: ")
#     num1, num2 = input_str.split(',')
#     print(num1, num2)
#     result = int(num1.strip()) / int(num2.strip())
# except SyntaxError as e:
#     print("Error: ", e)
# except ValueError as e:
#     print("Error: ", e)
# except ZeroDivisionError as e:
#     print("Error: ", e)
# else:
#     print(f"The result of {num1} / {num2} is: {result}")
# finally:
#     print("Finally block")
#
# try:
#     value = int(input("Enter a positive integer: "))
#     if value <= 0:
#         # raise 'ZeroDivisionError("That is not a positive number!")'
#         raise ZeroDivisionError("That is not a positive number!")
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)


# class CustomError(Exception):
#     def __init__(self, data):
#         self.data = data
#
#     def __str__(self):
#         return repr(self.data)


# def is_even(number):
#     if type(number) is not int:
#         raise CustomError("That is not a int number!")
#     return number % 2 == 0
#
#
# try:
#     user_input = input("Enter an integer: ")
#     if is_even(user_input):
#         print(f"{user_input} is even.")
#     else:
#         print(f"{user_input} is odd.")
# except CustomError as e:
#     print(e)
#     print("Invalid input! Please enter a valid integer.")

import logging

logging.basicConfig(filename="log_lesson11.log",
                    format='%(asctime)s - %(thread)d- %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


#
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def is_even(number):
    if type(number) is not int:
        logging.error(f"That is not a int number. value{number}!")
        raise CustomError(f"That is not a int number. value{number}!")
    return number % 2 == 0


while True:
    try:
        user_input = int(input("Enter an integer: "))
        logging.info(f"value: {user_input}")
        if is_even(user_input):
            print(f"{user_input} is even.")
        else:
            print(f"{user_input} is odd.")
    except CustomError as e:
        logging.info("Invalid input! Please enter a valid integer.")
        # print("Invalid input! Please enter a valid integer.")
    except ValueError as e:
        logging.error(e)
    else:
        break
