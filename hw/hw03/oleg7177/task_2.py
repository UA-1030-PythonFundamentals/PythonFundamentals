digit = 1234
product = (int(str(digit)[0])) * (int(str(digit)[1])) * (int(str(digit)[2])) * (int(str(digit)[3]))
print("product :",product)

digit = (int(str(digit)[3]+str(digit)[2]+str(digit)[1]+str(digit)[0]))
print(digit)

digit_list = [(int(str(digit)[0])),(int(str(digit)[1])),(int(str(digit)[2])),(int(str(digit)[3]))]
digit_list.sort(reverse=True)
print(digit_list)
