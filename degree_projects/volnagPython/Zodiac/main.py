from zodiac import zod


month_in = input('''
                 J - January, F - February , Ma - March,
                 A - April,  My - May,   Ju - June,
                 Jy - July,  Ag -August, S - September,
                 O - October, N - November, D - December \n
                 Enter your month of birth :
                 ''')
date_in = int(input('''\n
                 Enter your date of birth :
                 '''))
z = zod(month_in,date_in)

message = f"Ваш зоряний знак {z.upper()}."
   

d =len(message)
print("\u250C"+(d+3)*"\u2500"+"\u2510")
print(f"\u2502 Ваш зоряний знак {z.upper()}."+"  "+"\u2502")
print("\u2514"+(d+3)*"\u2500"+"\u2518")
#print("\u2518,\u2514,\u2502,\u2510,\u2500,\u250C,\u25CF")

#VN -- July 24, 2023
