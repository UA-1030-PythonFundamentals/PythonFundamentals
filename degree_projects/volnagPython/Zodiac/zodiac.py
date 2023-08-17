##Annual periods for all star signs.

def zod(month_in, date_in):
    '''Classification of all star signs'''


    if month_in == "Ma" and date_in in range(22,32):
        sign = "Aries"    
    elif month_in == "A" and date_in in range(1,20):
        sign = "Aries"

    elif month_in == "A" and date_in in range(20,31):
        sign = "Taurus"
    elif month_in == "My" and date_in in range(1,21):
        sign = "Taurus"

    elif month_in == "My" and date_in in range(21,32):
        sign = "Gemini"
    elif month_in == "Ju" and date_in in range(1,21):
        sign = "Gemini"

    elif month_in == "Ju" and date_in in range(21,32):
        sign = "Cancer"
    elif month_in == "Jy" and date_in in range(1,23):
        sign = "Cancer"

    elif month_in == "Jy" and date_in in range(23,32):
        sign = "Leo"    
    elif month_in == "Ag" and date_in in range(1,23):
        sign = "Leo"

    elif month_in == "Ag" and date_in in range(23,32):
        sign = "Virgo"    
    elif month_in == "S" and date_in in range(1,23):
        sign = "Virgo"
        
    elif month_in == "S" and date_in in range(23,31):
        sign = "Libra"
    elif month_in == "O" and date_in in range(1,23):
        sign = "Libra"
    
    elif month_in == "O" and date_in in range(23,32):
        sign = "Scorpio"
    elif month_in == "N" and date_in in range(1,22):
        sign = "Scorpio"

    elif month_in == "N" and date_in in range(22,31):
        sign = "Sagittarius"
    elif month_in == "D" and date_in in range(1,22):
        sign = "Sagittarius"
        
    elif month_in == "J" and date_in in range(1,20):
        sign = "Capricorn"
    elif month_in == "D" and date_in in range(22,32):
        sign = "Capricorn"
        
    elif month_in == "J" and date_in in range(20,32):
        sign = "Aquarius"
    elif month_in == "F" and date_in in range(1,19):
        sign = "Aquarius"
        
    elif month_in == "F" and date_in in range(20,30):
        sign = "Pisces"    
    elif month_in == "Ma" and date_in in range(1,21):
        sign = "Pisces"
    return sign


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



