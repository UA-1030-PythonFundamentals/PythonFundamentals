# c = int(input("Enter the temperature in Celsius: "))
# if c < -273.15:
#     print("Error: Temperature below absolute zero (-273.15°C)")
# else: print(c,"°C is equivalent to ",c*9/5+32,"°F")

# def stutter(word):
#     if len(word) <= 2:
#         print("oh",end="...\n")
#     else: print(word[:2],word[:2],word,sep="."*3,end="?")
# stutter("Fg")
#
# stutter("Fdjhljfhdk")

def X_O(word):
    X = 0
    O = 0
    for i in range (0,len(word)):
        if "x" == word[i]:
            X = X+1
        if "o" == word[i]:
            O = O+1
    if X or O > 0:
        print(X is O)
    else: print("x" and "o" not in word)
def makes10(num1,num2):
    if num2*num2 == num1:
        print("True", num2*num2)
    else: print("False")
makes10(4,2)

