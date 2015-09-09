def funNumbers(x, y, z):
    return x + y + z

def moreNumbers(a, b, c):
    funNumbers(x, y, z)
    return funNumbers(x, y, z) + a + b + c

def funname():
    print "What is your name?",
    name = raw_input()
    print name[0]

def names(s):
    space = s.index(" ")
    if space == 0:
        return False
    elif s.endswith(" "):
        return False
    else:
        print "Your first name is", s[0:space]
        print "Your last name is", s[space+1:]
        #return True

def squares(list1):
    newList = []
    for i in list1:
        newList.append(i**2)
    print list1
    return newList

def initials(list1):
    result = ""
    for i in range(len(list1)):
        result += list1[i][0]
    return result

def initials2(strings):
    result = ""
    for index in range(len(strings)):
        result += strings[index][0]
    return result

def initials3(strings): # using a for loop
    result = ""
    for s in strings:
        result += s[0]
    return result

def seqSearch(lis, target):
    for index in range(0, len(lis)):
        if lis[index] == target:
            return index
        
def revSearch(lis, target):
    for index in range (len(lis)-1, -1, -1):
        if lis[index] == target:
            return index
        
def binSearch(lis, target):
    lowIndex = 0
    highIndex = len(lis)-1
    while lowIndex <= highIndex:
        midIndex = (lowIndex + highIndex) //2
        if lis[midIndex] == target:
            return midIndex
        elif target < lis[midIndex]:
            highIndex = midIndex - 1
        else:
            lowIndex = midIndex + 1
    return None

# returns the first occurrence in a list using binary search
def firstBinSearch(lis, target):
    lowIndex = 0
    highIndex = len(lis)-1
    while lowIndex <= highIndex:
        midIndex = (lowIndex + highIndex) //2
        for index in range(lowIndex, midIndex):
            if lis[index] == target:
                return index
            else:
                lowIndex +1
        for index in range(midIndex, highIndex+1):
            if lis[index] == target:
                return index
            else:
                highIndex - 1
    return None            

def trinary(lis, target):
    lowIndex = 0
    highIndex = len(lis)-1
    while lowIndex <= highIndex:
        oneThird = (lowIndex + highIndex) // 3
        secondThird = oneThird*2
        if lis[oneThird] == target:
            return oneThird
        elif lis[secondThird] == target:
            return secondThird
        # start of the list - 1/3 of the list
        for index in range(lowIndex, oneThird):
            if lis[index] == target:
                return index
            else:
                lowIndex +1
        # from 1/3 - 2/3 of the list
        for index in range(oneThird, secondThird):
            if lis[index] == target:
                return index
            else:
                oneThird+1
            # from 2/3 to end of list
        for index in range(secondThird, highIndex+1):
            if lis[index] == target:
                return index
            else:
                highIndex - 1
    return None

# sorts in reverse
def bubbleSort(lis):
    for maxIndex in range(len(lis)-1, 0, -1):
        swapped = False
        for i in range(0, maxIndex):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1],lis[i]
                swapped = True
        if not swapped:
            return
        
# sorts from beginning of list
def bubbleSort2(lis):
    for maxIndex in range(0, len(lis)-1):
        swapped = False
        for i in range(0, len(lis)-1):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1],lis[i]
                swapped = True
        if not swapped:
            return

def selSort(lis):
    for m in range(0, len(lis)-1):
        minIndex = m
        for e in range(m+1, len(lis)):
            if lis[e] < lis[minIndex]:
                minIndex = e
        lis[m],lis[minIndex] = lis[minIndex],lis[m]

def selSort2(lis):
    for m in range(len(lis)-1, 0, -1):
        maxIndex = m
        for e in range(m-1, len(lis)):
            if lis[e] > lis[maxIndex]:
                maxIndex = e
        lis[m],lis[maxIndex] = lis[maxIndex],lis[m]

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram2(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

def print_hist(h):
    k = h.keys()
    k.sort()
    for c in k:
        print c, h[c]

def reverse_lookup(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    raise ValueError


def reverse(dictionary, val):
    valList = [] # creates an empty list to store all the keys in
    for key in dictionary:
            if dictionary[key] == val: #if the value of the key and the target
                valList.append(key)  #value are equal, add the key to the list
    return valList


def insertValue(linkedList, index, value):
    newNode = {'data':value}
    if index == 0: # if you want to insert at the beginning
        newNode['next'] = linkedList
        return newNode
    else:
        before = nthNode(linkedList, index-1) # before the point you want to insert
        if before ==None:
            print "Error"
            return linkedList
        else:
            after = before['next'] #going to come after the new entry
            before['next'] = newNode # changes into the new entry
            newNode['next'] = after #makes the new entry point to the one it was just placed in front of
            return linkedList

def nthNode(linkedList, index):
    if index < 0 or linkedList == None:
        return None
    node = linkedList
    count = 0
    while count < index:
        node = node['next']
        if node == None:
            return None
        count += 1
    return node

def insertValue2(linkedList, index, value):
    newNode = {'data':value}
    if index == 0:
        newNode['next'] = linkedList
        return newNode
    else:
        before = nthNode(linkedList, index-1)
        if before == None:
            print "error"
            return linkedList
        else:
            after = before['next']
            before['next'] = newNode
            newNode['next'] = after
            return linkedList

def createList(plist):
    linkedList = None
    for index in range(len(plist)-1, -1, -1):
        linkedList = insertValue(linkedList,0, plist[index])
    return linkedList

def listString(linkedList):
    description = "["
    isFirst = True
    node = linkedList
    while node != None:
        if isFirst:
            isFirst = False
        else:
            description += ","
        description += str(node['data'])
        node = node['next']
    description += "]"
    return description

def printList(linkedList):
    print listString(linkedList)
    
def addAfter(linkedList, val1, val2):
    newNode = {'data': val2} #call findNode
    #findNode(linkedList, val1)
    while linkedList['data'] != val1:
        ptr = linkedList['next']
        return ptr
    before = {'data': val1}
    after = before['next']
    newNode['next'] = linkedList
    before['next'] = newNode
    return linkedList

def findNode(linkedList, value):
    while linkedList['next'] != value:
        ptr = ptr['next']
    return ptr

def swap(link, index):
    if index < 0 or index > len(link):
        return link
    else:
        before = nthNode(link, index)
        after = nthNode(link, index+1)
        before['data'],after['data'] = after['data'], before['data']
        return printList(link)

def movePos(lst, position):
    toMove = nthNode(lst, position)
    after = lst['next']
    firstNode = {'data':toMove}
    before = firstNode['data']
    before['next'] = after
    return lst
    
lis  = [1,7,5,13]
linked = createList(lis)

lst = [2,-3,5,-6,-7,1,3,2]

def countNegs(lst):
    count = 0
    for i in lst:
        if i < 0:
            count += 1
    return count
