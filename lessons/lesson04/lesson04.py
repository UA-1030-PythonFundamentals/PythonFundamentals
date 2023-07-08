# print(not 1)
# print(not 0)
# print(not [])
# print(not [1, 2, 3])
# is_false = [False, None, 0, 0.0, "", [], (), {}]
# my_list = []
# if len(my_list) != 0:
#     pass
# for element in is_false:
#     if element:
#         print(True)
#     else:
#         print(False)
#
# is_true = [True, 1, 0.01, " ", [1], (1,), {1}, {1:1}]# etc
# for element in is_true:
#     if element:
#         print(True)
#     else:
#         print(False)

# print(True and True)
# print(True and True and False)
# print(True and True and [])
# print(True and True and [1] and 999)
# print(True and True and [1] and 999)
# print(0 or [] or [1] or {})
# print(0 or [] or [] or {})
# print(1 and [[]] or 11 and [])


# l1 = [2, 1]
# l2 = [1, 2]
# print(id(l1), id(l2))
# print(l1 is l2)
# print(l1 == l2)

# l = [1, 2, 3, "abc", [1, 2]]
# print(1 in l)
# print("abc" in l)
# print("a" in l)
# print([1, 2] in l)
# print([2, 1] not in l)
# text = input("set text:")
# my_name = None
# if text:
#     my_name = "text"
#     print(f"text is: {text}")
#     print(f"len: {len(text)}")
# print("end")
# print(my_name)

# text = input("set text:")
# my_name = None
# if text:
#     print(f"text is: {text}")
#     print(f"len: {len(text)}")
# else:
#     print("text is empty")
# print("end")

# age = int(input("set age:"))
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')
#
# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')


# age = int(input("set age:"))
# if age >= 18 and age < 65:  # 18 65g
#     print("is worker")
# else:
#     print("humen is yong or old")
#
# if 18 <= age < 65 < 88 < 9999:  # 18 65g
#     print("is worker")
# else:
#     print("humen is yong or old")
#
# age = int(input("set age:"))
# text = None
# if age > 15:
#     text = "Worker"
#
# print(text)
#
# # text = "Worker" if age > 15 else None
#
# # text = age > 15 ? "Worker" : None

# age = int(input("set age:"))
# TEXT = 'kid' if age < 12 else 'teenager' if age < 18 else "adult" if age < 50 else 'you are not old'
# print(TEXT)


# status = int(input("set http status code:"))


# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
# if status == 400:
#     print("Bad request")
# elif status == 401:
#     print("Unauthorized")
#     print("Unauthorized")
# elif status == 403:
#     print("Forbidden")
# elif status == 404:
#     print("Not found")
# else:
#     print("Other error")

# match status:
#     case 400:
#         print("Bad request")
#     case 401 | 403 as error:
#         print(f'{error} is authentication error {status}')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")

# my_match = {
#     400: "Bad request",
#     401: "Unauthorized",
#     403: "Forbidden"
# }
#
# print(my_match.get(status, "Other error"))
# def load(l):
#     print(l)
#
#
# def save(l, f):
#     print(l, f)
#
#
# my_values = [
#     ("load", "link"),
#     ("save", "link", 15),
#     ("save", "link", [12, 17], 17, 22),
#     "aaa"
# ]
# for values in my_values:
#     match values:
#         case "load", link:
#             print('case "load", link:')
#
#             load(link)
#         case l, link, 15:
#             print('case l, link, 15:')
#
#             print(l, link)
#         case "save", link, filename:
#             print('case "save", link, filename')
#             save(link, filename)
#         case "save", link, *filenames:
#             print('case "save", link, *filename')
#             for filename in filenames:
#                 save(link, filename)
#         case _:
#             print("def")
#             print(values)
