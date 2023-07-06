# # # list
# # l = list()
# # print(l, type(l))
# # l = list("test")
# # print(l, type(l))
# # l = list(("asdd", [1, 2, 3], 15, {1, 2, 3}))
# # print(l, type(l))
# # # l = list(45) # error
# # l = []
# # print(l, type(l))
# # l = ["isdbvhidsb"]
# # print(l, type(l))
# # l = ["asdd", [1, 2, 3], 15, {1, 2, 3}]
# # print(l, type(l))
# # print(l[0], type(l[0]))
# # print(l[3], type(l[3]))
# # # print(l[5], type(l[5])) # error
# # print(l[-1], l[-2]) # error
# # print(l[0:3])
# # print(l[::2])
# # print(l)
# # l[2] = 999
# # print(l)
# # print(l[0][2])
# # print(l[1][1])
#
# print([method for method in dir(list) if not method.startswith("_")])
# l = ["asdd", [1, 2, 3], 15, {1, 2, 3}]
# # l.append("new")
# # l.append(111)
# # l.append([1, 2, 3, 4, 5])
# # print(id(l), l)
# # # l.clear()
# # # print(id(l), l)
# # # l = []
# # # print(id(l), l)
# # print(l)
# # ll = l[-1]
# # print(ll)
# # ll.append(999)
# # print(ll)
# # print(l)
# # # ll.clear()
# # # print(ll)
# # # print(l)
# # ll = []
# # print(ll)
# # print(l)
# # ll = l.copy()
# # print(id(l), l)
# # print(id(ll), ll)
# # lll = l[:]
# # print(id(lll), lll)
# # l[0] = "test"
# # print(l)
# # print(ll)
# # print(lll)
# # l[1].append(99)
# # ll[2] = ll[2]**3
# # print(l)
# # print(ll)
# # print(lll)
# # import copy
# # dl = copy.deepcopy(l)
# # print(dl)
# # l[1].append(888)
# # print(l)
# # # print(ll)
# # # print(lll)
# # # print(dl)
# # print(l.count(15))
# # print(l)
# # l.append("test")
# # l.extend("test")
# # l.extend((1, 2, 3))
# # print(l)
# # l = [1, 2]
# # ll = [3, 4]
# # lll = l + ll
# # print(id(l), l)
# # print(id(ll), ll)
# # print(id(lll), lll)
# # l = l +[17]
# # print(id(l), l)
# l = ['asdd', 10, 99, [1, 2, 3], 15, 10, {1, 2, 3}, 'test', 't', 'e', 's', 't', 10, 2, 3]
# print(l)
# print(l.index(10))
# print(l.index(10, 2))
# print(l.index(10, 6))
# # print(l.index(10, 6, 11))
# l.insert(1, "My")
# print(l)
# l.insert(100, "My")
# l.insert(-100, "-My")
# print(l)
# e = l.pop()
# print(e, l)
# e = l.pop(3)
# print(e, l)
# # e = l.pop(30) # error
# e = l.remove(10)
# print(e, l)
# l.reverse()
# print(l)
#
#
# def my_s(element):
#     if type(element) is int:
#         return element
#     else:
#         return len(element)
#
#
# # l.sort(key=lambda element: element if type(element) is int else len(element))
# print(l)
# ll = list(reversed(l))
# print(l)
# print(ll)
# ll = sorted(l, key=my_s)
# print(l)
# print(ll)
# # print(all(l))
# # l.append("")
# # print(all(l))
# # l.clear()
# # l.append("")
# # l.append("x")
# # print(any(l))
# print(list(enumerate(l)))
# print(max(l, key=my_s))
# l = [1, 32, 6, 32, 6]
# print(sum(l))
# # l = [[1, 32], [6, 32, 6]]# error
# # print(sum(l))

# ## tuple
# t = tuple()
# print(type(t), t)
# t = tuple("test")
# print(type(t), t)
# t = ()
# print(type(t), t)
# t = (1,)
# print(type(t), t)
# t = (1, 3)
# print(type(t), t)
# t = (1, 32, 6, 32, 6)
# print(t[3])
# # t[1] = 15 #error
# t = (1, 32, 6, 32, 6, [1,2,3])
# t[5].append(4)
# t[5][2] = 99
# print(t)
# print([method for method in dir(tuple) if not method.startswith("_")])
#
#
# l = [i**i for i in range(1000)]
# t = tuple(l)
# print(l.__sizeof__() )
# print(t.__sizeof__())

# ### set
# s = set()
# s = set("bgfhsbsdkbrg;kjserilghsjgdfjksbfgjhe")
# print(s)
# s = set([(1,2,3), (1,2,3), (1,2,3)])
# print(s)
# s = {1,2,3,1,2,3,4,5,1,2,4}
# print(type(s), s)
# print([method for method in dir(set) if not method.startswith("_")])
# e = s.pop()
# print(e)
# s.update("sadvfdsfds")
# s.add("sadvfdsfds")
# print(s)

### dict
d = dict()
d = dict(((1, ""), (2, 2), ("3", 3)))
print(d)
d = {}
d = {
    1: "",
    "22": 33,
}
print(d)
print([method for method in dir(dict) if not method.startswith("_")])
d["dsfds"] = 15
print(d)
d["22"] = 15
print(d)
print(d["22"])
# print(d["222"]) #error
print(d.get("22"))
print(d.get("222"))
print(d.get("222", "foo"))
print(d.items())
print(d.keys())
print(d.values())
for key, value in d.items():
    print(key, value)

dd = d.setdefault((1, 2, 3, 4, 5, 6), "test")
print(d, dd)
d.fromkeys((1, 2, 3, 4, 5, 6), "test")
print(d)
# d[[1,2]]
d[(1,2)] = 1
d[(1,2)] = 1
