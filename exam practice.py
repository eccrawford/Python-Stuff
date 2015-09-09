#Exam practice

def isPerfect(n):
    if n < 2:
        return False
    x = 0
    r = 0
    for x in range(1,n+1):
        if n%x == 0:
            r = r + x
            if x == n:
                if r == 2*n:
                    return True
                else:
                    return False
def pyTriple(n):
    c = n**2
    for a in range(1,n):
        for b in range(1,n):
            if a**2 + b**2 == c:
                triples = [a,b,n]
                print triples
    print "no triples found"

def recSelSort(lis):
    if len(lis) == 0 or len(lis) == 1:
        return lis
    elif len(lis) == 2:
        if lis[0] > lis[1]:
            lis[0],lis[1] == lis[1],lis[0]
            return lis
        else:
            return recSelSort(lis[:])
        
def count(lis, target):
    return lis.count(target)

def count2(lis, target):
    if len(lis) == 0:
        return 0
    else:
        return count(lis, target)
    
def cleanup(numlis):
    i = 0
    while i < len(numlis)-1:
        if numlis[i] == numlis[i+1]:
            del numlis[i]
        else:
            i +=1
    return numlis

def backwardsBinary(lis, target):
    low = 0
    high = len(lis)-1
    while low <= high:
        mid = (low+high)//2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            high = mid-1
        else:
            low = mid+1
    return -1

from random import randint
def dieToss():
    die1 = randint(1,6)
    die2 = randint(1,6)
    die3 = randint(1,6)
    rolls = 1
    ones = 0
    fives = 0

    while die1 != die2 and die2 != die3 and die3 != die1:
        #Terminates if any two dice are the same
        print "Roll", rolls, "-", die1, die2, die3
        if die1 == 1 or die2 == 1 or die3 == 1:
            ones +=1
        if die1 == 5 or die2 == 5 or die3 == 5:
            fives += 1
        #counts the number of 1s and 5s until two die are the same
        rolls += 1
        die1 = randint(1,6)
        die2 = randint(1,6)
        die3 = randint(1,6)
    print "Roll", rolls, "-", die1, die2, die3
        
    print "Number of rolls (before termination): ", rolls-1
    print "Number of 1's rolled:", ones
    print "Number of 5's rolled:", fives

def stringMatch(lis, char):
    for word in lis:
        if char in word:
            print word, word.count(char)
