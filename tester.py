def calc1(): #finds a solution to 43x = 12 (mod 73)
    x = 43
    for i in range(2, 74):
        y = (x*i)%73
        print x,"*",i,"=",y
        if y == 12:
            break # I already know there should be 1 solution
        
def calc2(): #checks for a solution to 10x = 99 (mod 125)
    x=10
    for i in range(2, 126):
        y = (x*i)%125
        #print x,"*",i,"=",y
        if y == 99:
            break #there should be none, so it will never break
        
def calc3(): #finds solutions to 10x = 25 (mod 125). There should be 5 in total
    x=10
    sol=0
    for i in range(2,126):
        y = (x*i)%125
        if y == 25:
            print x,"*",i,"=",y
            sol += 1
            print "SOLUTION #", sol



def generalCases(n, c, m): # solutions to nx = c (mod m)
    sol=0
    for i in range(2, m+1):
        y=(n*i)%m
        # print n,"*",i,"=",y
        if y == c:
            print n,"*",i,"=",y
            sol += 1
            print i, "is solution #",sol
    if sol == 0:
        print "No Solutions Exist"
            
    
