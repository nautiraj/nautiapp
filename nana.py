# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(iname):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {iname}')  # Press Ctrl+F8 to toggle the breakpoint.


print_hi("hi pycharm")


def days_to_hour(num_of_days):
    calc_to_units = 24
    name_of_units = 'hours'
    return f"{num_of_days} days to {name_of_units} are {num_of_days*calc_to_units} {name_of_units}"


def validate_user_input():
    try:
        user_input_days = int(user_input)
        if user_input_days > 0:
            results = days_to_hour(user_input_days)
            print(results)
        elif user_input_days == 0:
            print("please enter valid positive number, 0 can not be converted")
        else:
            print("negative number not allowed")
    except ValueError:
        print("your input is not a valid number")


user_input = ""
while user_input != 'exit':
    user_input = (input("provide number of day to convert!\n"))
    validate_user_input()
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/