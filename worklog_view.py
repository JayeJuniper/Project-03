import os
import csv
import re


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class View():
    '''Allows the user of the script to find a previous entry via four
    options: find by date, find by time spent, find by exact search, and find
    by pattern.
    '''

    def __init__(self):
        with open('worklog.csv', newline='') as csvfile:
            # compose lines as dicts
            log_reader = csv.DictReader(csvfile, delimiter=',')
            self.entries = list(log_reader)
            self.proxy = []

    def print_log(self, entry):
        print('''
        Log Title: {}
        Time Worked: {}
        Notes: {}
        Date Logged: {}
        '''.format(entry['title'], entry['time worked'], entry['notes'],
                   entry['date']))

    def search_date(self):
        # When finding by date, I should be presented with a list of dates
        # with entries and be able to choose one to see entries from.
        clear()
        print("Find by date. Please enter a following date to view it's log:")

        for entry in self.entries:
            if entry['date'] not in self.proxy:
                self.proxy.append(entry['date'])
        dates = sorted(self.proxy)

        for date in dates:
            print(" "*8 + date)

        search = input('> ')
        clear()
        print("Selected entries are as follows:")
        for entry in self.entries:
            if entry['date'] == search:
                View().print_log(entry)

        input('\nPress ENTER to return to directory. ')

    def search_time_worked(self):
        # When finding by time spent, I should be allowed to enter the number
        # of minutes a task took and be able to choose one to see entries from
        clear()
        print("Find by time worked. Please enter a following time to view it'\
s log:")

        for entry in self.entries:
            if entry['time worked'] not in self.proxy:
                self.proxy.append(entry['time worked'])

        times = sorted(self.proxy)
        for time in times:
            print(" "*8 + time)

        search = input("\n> ")
        clear()
        print("Selected entries are as follows:")
        for entry in self.entries:
            if entry['time worked'] == search:
                View().print_log(entry)

        input('Press ENTER to return to directory. ')

    def search_exact_string(self):
        # When finding by an exact string, I should be allowed to enter a
        # string and then be presented with entries containing that string
        # in the task name or notes.
        clear()
        search = input(("Find by searched term. Please enter an exact term to\
         find matching logs:\n> "))

        print("Selected entries are as follows:")
        for entry in self.entries:
            if entry['title'] == search:
                View().print_log(entry)
            elif entry['notes'] == search:
                View().print_log(entry)

        input('Press ENTER to return to directory. ')

    def search_pattern(self):
        # When finding by a pattern, I should be allowed to enter a regular
        # expression and then be presented with entries matching that pattern
        # in their task name or notes.
        clear()
        search = input(("Find by pattern. Please enter a a term to match by:\
        \n> "))

        search_proxy = r'' + search

        print("Selected entries are as follows:")
        for entry in self.entries:
            if (re.search(search_proxy, entry['title']) or
                re.search(search_proxy, entry['notes'])):
                View().print_log(entry)

        input('Press ENTER to return to directory. ')
