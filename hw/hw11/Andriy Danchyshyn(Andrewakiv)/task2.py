import logging


def day():
    num = input('Enter number to get the day: ')
    dct = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Tuesday',
           '5': 'Friday', '6': 'Saturday', '7': 'Sunday'}
    if num in dct:
        return dct[num]
    else:
        logging.error('Enter number from 1 to 7')


print(day())
