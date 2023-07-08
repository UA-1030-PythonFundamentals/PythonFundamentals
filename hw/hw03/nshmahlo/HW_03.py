# ST = '''The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# '''
# r = ST.count('never')
# b = ST.count('better')
# z = ST.count('is')
# print('Number of occurrence of better: %d' % b)
# print('Number of occurrence of never: %d'% r)
# st = ST.upper()   #uppercase
# print(st)
# ss = ST.replace('i','&')
# print(ss)
# #task3
# K = str(input('Enter your four-digit natural number: '))
# k1=int(K[0])
# k2=int(K[1])
# k3=int(K[2])
# k4=int(K[3])
# print('product of your number digit is ',k1*k2*k3*k4)
# print(K[::-1])
# print(''.join(sorted(K)))
# # task#4
# h=(23)
# l=(56)
#
# print(h,l)
# h=h+l
# l=h-l
# h=h-l
# print (h,l)

def vol_shell(r1,r2):
    PI = 3.14
    return round(4/3*PI*(r1**3-r2**3),2)
print(vol_shell(4,3))
