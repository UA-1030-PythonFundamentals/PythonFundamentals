# Practical Task # 3 - June 21, 2023
file = open('ZenPhilosophy.txt')
s = file.read()

print("\n")
print("There are/is ",s.count("better"), '"better" word(s) in Zen Philosophy.')
print("There are/is ",s.count("never"), '"never" word(s) in Zen Philosophy.')
print("There are/is ",s.count("is"), '"is" word(s) in Zen Philosophy.\n\n')
    #Capitalising s string
S = s.upper()
print(S,"- Here is Zen in capital letters.\n")

    #Checking the specific line
lin1 = input('''Zen Phylosophy text has 56 lines.
Which line are you interested in? \n''')
    
i = s.index(lin1)
I = int(lin1)
lin2 = I + 1
lin2 = str(lin2)
j = s.index(lin2)
    #print("The indices for that line are :","\n",i,"\n",j)

row = s[i:j]
print("\n","Your line reads: ",row)

print("There are/is ",row.count("better"), '"better" word(s) in your line.')
print("There are/is ",row.count("never"), '"never" word(s) in your line.')
print("There are/is ",row.count("is"), '"is" word(s) in your line.\n\n')
    #Replacing "i" with "&"
r = s.replace("i","&")
print(r)
#VN

