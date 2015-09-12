def calc1(): #finds a solution to 19x = 99 (mod 125)
    x = 19
    for i in range(19, 126):
        y = (x*i)%125
        print x,"*",i,"=",y
        if y == 99:
            break # I already know there should be 1 solution
        
def calc2(): #checks for a solution to 10x = 99 (mod 125)
    x=10
    for i in range(10, 126):
        y = (x*i)%125
        print x,"*",i,"=",y
        if y == 99:
            break #there should be none, so it will never break
        
def calc3(): #finds solutions to 10x = 25 (mod 125). There should be 5 in total
    x=10
    sol=0
    for i in range(10,126):
        y = (x*i)%125
        print x,"*",i,"=",y
        if y == 25:
            sol += 1
            print "SOLUTION #", sol 
