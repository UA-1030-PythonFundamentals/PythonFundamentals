# f = open("C:\data\github\PythonFundamentals\lessons\lesson14\data.txt")
# f = open("data.txt")
# print(f.read())
# f.close()
#
# f = open("in/users.txt")
# print(f.read())
# f.close()
# f = open("../../hw/hw01/AnaDob/task 1.py")
# print(f.read())
# f.close()
# print([method for method in dir(f) if not method.startswith("_")])

# f = open("out/data.txt", "a")
# f.writelines("test1\n")
# f.writelines("test2\n")
# f.writelines("test3\n")
# f.close()
# try:
#     f = open("in/users.txt", "r")
#     print(f.read())
#     # f.writelines("jhdsvjfd")
# except:
#     pass
# finally:
#     f.close()
# f = open("in/users.txt", "r")
# print(f.tell())
# line = f.readline()
# while line:
#     print(line)
#     print(f.tell())
#     line = f.readline()
#     f.seek(0)
# else:
#     print(f"end=<{line}>")
# with open("in/users.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line)
#         line = file.readline()
#
# with open("in/users.txt", "r") as file1, open("data.txt", "r") as file2:
#         line = file1.readline()
#         while line:
#             print(line)
#             line = file1.readline()
#
#         line = file2.readline()
#         while line:
#             print(line)
#             line = file2.readline()



