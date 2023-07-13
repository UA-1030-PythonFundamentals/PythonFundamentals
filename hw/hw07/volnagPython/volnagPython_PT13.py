##Task3. Write a function that calculates the number of characters
##included in a given string
##• input: "hello"
##• output: {"h":1, "e":1,"l":2,"o":1} --- PT13 from HW07, July 11, 2023

#word = input("Enter your word \n :")

def simb_occurence(word):
    '''The function calculates the number of character's  occurence
    in the key word. It returns the result in
    a dictionary form : [key}:value.'''

    ln = list(word)     #Converts the string into a list
    lns = set(ln)       #Gives the set of unique chracters 
    lnsi = list(lns)    #Gives the list of unique chracters 
   
    cnt= list()

    i = 0
    for i in range(len(lnsi)):
        cnt.append(ln.count(lnsi[i]))
        i+=1

    ds = zip(lnsi,cnt)  #Gives the tuple from combining lnsi and cnt
    return dict(ds) 
