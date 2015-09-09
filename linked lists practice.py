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
    node = linkedList
    count = 0
    while count < index:
        node = node['next']
        if node == None:
            return None
        count += 1
    return node

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
    newNode = {'data': val2}
    ptr = linkedList
    while ptr != None and ptr['data'] != val1:
        ptr = ptr['next']
    if ptr == None:
        return
    newNode['next'] = ptr['next']
    ptr['next'] = newNode
