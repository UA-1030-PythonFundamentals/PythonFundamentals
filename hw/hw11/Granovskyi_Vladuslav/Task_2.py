import logging
def days_of_week():
    number = input('Enter number to get the day: ')
    week = {'1': 'Monday', '2': 'Tuesday',
            '3': 'Wednesday', '4': 'Tuesday',
            '5': 'Friday', '6': 'Saturday',
            '7': 'Sunday'}
    if number in week:
        return week[number]
    else:
        logging.error("Error")

print(days_of_week())