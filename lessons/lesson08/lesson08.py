# # # print(__name__)
# # # print(__package__)
# # # print(__file__)
# # # print(dir())
# # import math
# # #
# # # print(id(math.e), math.e)
# # # print(id(math.pi), math.pi)
# # # from math import (pi,
# # #                   e,
# # #                   sin)
# # #
# # # print(id(e), e)
# # # print(id(pi), pi)
# # #
# # # import module_l1
# # # print(__name__)
# # import sys
# from pprint import pprint
# # sys.path.append("C:\data\github\PythonFundamentals")
# # pprint(sys.path)
# # from hw.hw06.vladimircity import task1
# #
# # if __name__ == "__main__":
# #     print("run lesson08.py")
# #     print(math)
#
#
# print(dir())
# import module_l1
# from math import pi as PI, e, tau as T
# print(dir())
# print(PI)
# pi = 17
# print(pi)
# print(PI)
# print(e)
# print(T)
# pprint(dir())
# pprint(locals())
# from lessons.lesson07.lesson07 import l
# print(l)
# import lessons.lesson07.lesson07
# print(lessons.lesson07.lesson07.l)
# import lessons.lesson07.lesson07 as l7
# print(l7.l)
from fincalc.simper import *
print(dir())
from fincalc.simper import _sin2, __sin2
print(dir())
import math