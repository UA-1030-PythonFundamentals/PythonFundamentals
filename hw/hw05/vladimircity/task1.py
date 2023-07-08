# Turn list values to float type
def main():
    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for index in range(len(integer_list)):
        integer_list[index] = float(integer_list[index])

    print(integer_list)


if __name__ == '__main__':
    main()
