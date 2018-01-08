import sys
import os

from worklog_entry import Entry
from worklog_view import View


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def directory():
    '''Enables user to submit or view a work log. When submitting a work log,
    the user can add task names, the duration in minutes, and any additional
    notes which need to be recorded. furthermore, the user will be able to
    search submitted entries by date, time spent, exact search or by pattern.
    '''

    clear()
    entry_choice = None

    while entry_choice is None:
        # Choose to make a new entry or view an old one
        entry_choice = input('''Welcome to this work log directory. Would you like to:
      1 - Make a new entry
      2 - View an old entry
      3 - Quit
      \n> ''')
        if entry_choice not in ['1', '2', '3']:
            clear()
            print("Invalid selection, Try again.")
            entry_choice = None

    if entry_choice == '1':
        # make an entry
        Entry().new()
        clear()
        input("Your entry has been logged, press any key to return to the dir\
ectory. ")

    if entry_choice == '2':
        # view entries
        view_menu()
        directory()

    if entry_choice == '3':
        # quit
        clear()
        print("Good Bye.")
        sys.exit()

    directory()


def view_menu():
        '''This is the directory for all view functions, allowing the user to\
        view worklogs
        '''
        
        clear()
        view_choice = None
        while view_choice is None:
            view_choice = input('''How would you like to view entries?
        1 - Find by date.
        2 - Find by time spent.
        3 - Find by exact search.
        4 - Find by pattern.
        5 - Return to directory.
> ''')
            if view_choice not in ['1', '2', '3', '4', '5']:
                clear()
                print("Invalid selection, please try again.")
                view_choice = None

        if view_choice == '1':
            View().search_date()

        if view_choice == '2':
            View().search_time_worked()

        if view_choice == '3':
            View().search_exact_string()

        if view_choice == '4':
            View().search_pattern()

        if view_choice == '5':
            pass


if __name__ == "__main__":
    directory()
