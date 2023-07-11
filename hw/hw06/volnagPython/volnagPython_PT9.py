##Task1. In the range from 1 to 10 determine
##• even numbers that are divisible by 2,
##• odd numbers, which are divisible by 3,
##• numbers that are not divisible by 2 and 3.-- PT9 HW6-- July 4, 2023
print(70*("*"))

num = list(range(1,11,1))
odd_num = list()
even_num = list()
unq_num = []

print("Initial set of numbers =>", num)

for k in num:

  if not(k%2 == 0) and not(k%3 == 0):
        unq_num.append(k)
  elif k%3 == 0 and not(k%2 == 0):
        odd_num.append(k)
  elif k%2 == 0:
        even_num.append(k)

  else:
        print("-----No required numbers!-----")
print(70*("*"))
print("Our divisible on 2 numbers :",even_num)
print("Our divisible on 3 numbers :",odd_num)
print("Prime numbers :",unq_num)
print(70*("*"))
#VN
