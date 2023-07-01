s = []

while len(s) < 5:

        s.append((int(input("Enter only int numbers 5 times: "))))

print("You entered: ", s)
for i in range(len(s)):
                
        s[i] = float(s[i])
                
      
        
print("Your list in float type: ", s)