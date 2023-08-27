##Dates for star signs.

def zod(month_in, date_in):
    '''Classification of all star signs'''

    global sign
    sign = None
    
    if month_in == "Ma" and date_in in range(22,32):
        sign = "Овен"
    elif month_in == "A" and date_in in range(1,20):
        sign = "Овен"

    elif month_in == "A" and date_in in range(20,31):
        sign = "Телець"
    elif month_in == "My" and date_in in range(1,21):
        sign = "Телець"

    elif month_in == "My" and date_in in range(21,32):
        sign = "Близнюки"
    elif month_in == "Ju" and date_in in range(1,21):
        sign = "Близнюки"

    elif month_in == "Ju" and date_in in range(21,32):
        sign = "Рак"
    elif month_in == "Jy" and date_in in range(1,23):
        sign = "Рак"

    elif month_in == "Jy" and date_in in range(23,32):
        sign = "Лев"
    elif month_in == "Ag" and date_in in range(1,23):
        sign = "Лев"

    elif month_in == "Ag" and date_in in range(23,32):
        sign = "Діва"
    elif month_in == "S" and date_in in range(1,23):
        sign = "Діва"
        
    elif month_in == "S" and date_in in range(23,31):
        sign = "Терези"
    elif month_in == "O" and date_in in range(1,23):
        sign = "Терези"
    
    elif month_in == "O" and date_in in range(23,32):
        sign = "Скорпіон"
    elif month_in == "N" and date_in in range(1,22):
        sign = "Скорпіон"

    elif month_in == "N" and date_in in range(22,31):
        sign = "Змієносець"
    elif month_in == "D" and date_in in range(1,22):
        sign = "Змієносець"
        
    elif month_in == "J" and date_in in range(1,20):
        sign = "Козоріг"
    elif month_in == "D" and date_in in range(22,32):
        sign = "Козоріг"
        
    elif month_in == "J" and date_in in range(20,32):
        sign = "Водолій "
    elif month_in == "F" and date_in in range(1,19):
        sign = "Водолій "
        
    elif month_in == "F" and date_in in range(20,30):
        sign = "Риби"
    elif month_in == "Ma" and date_in in range(1,21):
        sign = "Риби"
    elif sign == None:
        sign = "Будь-ласка, введіть правильну дату..."
    return sign

##zod("F",32)
##print(sign)
##Aries star sign dates: March 21 – April 19
##Taurus star sign dates: April 20 – May 20
##Gemini star sign dates: May 21 – June 20
##Cancer star sign dates: June 21 – July 22
##Leo star sign dates: July 23 – August 22
##Virgo star sign dates: August 23 – September 22
##Libra star sign dates: September 23 – October 22
##Scorpio star sign dates: October 23 – November 21
##Sagittarius star sign dates: November 22 – December 21
##Capricorn star sign dates: December 22 – January 19
##Aquarius star sign dates: January 20 – February 18
##Pisces star sign dates: February 19 – March 20



