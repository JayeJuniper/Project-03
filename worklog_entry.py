import datetime
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Entry():
    '''Allows the user to create new work log entries.
    '''

    def new(self):
        '''Allows the user to enter a new work log. The user should be able to
        provide a task name, a number of minutes spent working on it, and any
        additional notes they want to record.
        '''

        log_title = None
        log_duration = None
        log_notes = None

        clear()
        print("You selected to create a new entry.")

        while log_title is None:
            log_title = input("Name your worklog.\n> ")
            if log_title.isspace() is True or log_title == '':
                clear()
                print("Entry is empty. Please try again.")
                log_title = None

            for letter in log_title:
                if letter == ',':
                    clear()
                    print("Please avoid the use of commas, try again.")
                    log_title = None

        while log_duration is None:
            try:
                log_duration = int(input("Type the duration you wish to recor\
d (in minutes).\n> "))
            except ValueError:
                clear()
                print("Invalid time, make sure you round to the nearest whole\
 minute.")
                log_duration = None

            if log_duration not in range(1, 1440):
                clear()
                print("Invalid time, please try again.")
                log_duration = None

        while log_notes is None:
            log_notes = input("Record any additional notes for this time peri\
od.\n> ")
            for letter in log_notes:
                if letter == ',':
                    clear()
                    print('Please avoid the use of commas, try again.')
                    log_notes = None

        log_date = datetime.datetime.now()
        log_record = ','.join([str(log_date), log_title, str(log_duration),
                               log_notes])

        try:
            with open("worklog.csv", 'x') as csvfile:
                csvfile.write("date,title,time worked,notes")
            with open("worklog.csv", 'a') as csvfile:
                csvfile.write("\r\n"+log_record)
        except FileExistsError:
            with open("worklog.csv", 'a') as csvfile:
                csvfile.write("\r\n"+log_record)
