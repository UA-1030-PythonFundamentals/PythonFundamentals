# Practical Task #4 - June 23,2023
s = input("Enter a four digit integer number: \n")

s1 = int(s[0]);s2 = int(s[1]);s3 = int(s[2]);s4 = int(s[3])

list=[s1,s2,s3,s4]

prod =list[0]*list[1]*list[3]*list[2]
print("Result of multiplication of your numbers is \n",prod)

r = list[::-1]
print("Numbers are listed in reverse order : \n",r)

list.sort()
print("Numbers are sorted in ascending order : \n",list)
#VN
