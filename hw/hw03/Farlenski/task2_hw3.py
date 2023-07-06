number = int(input("Enter you number: "))

product = int(str(number)[0]) * int(str(number)[1]) * \
        int(str(number)[2]) * int(str(number)[3])

reverse = int(str(number)[::-1])

sort = sorted(str(number))
ascending = "".join(sort)

out = f"Product: {product}\nReverse: {reverse}\nAscenging order: {ascending}"
print(out)
    