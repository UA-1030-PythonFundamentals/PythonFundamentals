import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

try:
    day = {
        1:"Monday", 
        2:"Tuesday", 
        3:"Wednesday", 
        4:"Thursday", 
        5:"Friday", 
        6:"Saturday", 
        7:"Sunday"
    }
    d = int(input("Enter the day of the week number (1-7): "))

    if d > 7 or d < 1:
        logging.info("You entered not 1-7")

    else:    
        print(f"{d} day of week is {day.get(d)}")

except ValueError:
    logging.error("You entered not integer number")