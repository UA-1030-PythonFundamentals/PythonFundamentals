zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

zen_lines = zen.split('\n')
lines = len(zen_lines)
# print(lines)
print('Python Zen:')
print()
print(zen)
print()
print(f"Enter string number between 1 and {lines}:")

line = int(input())

s = zen_lines[line - 1]
print('Given line:')

print()
print(s)
print()

print(f"Word 'better' found {s.count('better')} times")
print(f"Word 'never' found {s.count('never')} times")
print(f"Word 'is' found {s.count('is')} times")

print()
print('Python Zen in uppercase:')
print()
print(zen.upper())

print()
print('Python Zen replaced:')
print()
print(zen.replace('i', '&'))