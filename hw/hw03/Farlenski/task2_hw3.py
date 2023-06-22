number = int(input("Enter you number: "))

product = 1
for i in str(number):
    product *= int(i)

reverse = int(str(number)[::-1])

sort = sorted(str(number))
ascending = "".join(sort)

out = f"Product: {product}\nReverse: {reverse}\nAscenging order: {ascending}"
print(out)
    