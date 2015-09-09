def delLeaves(tree):
    if tree == None:
        return None
    elif tree['left'] != None or tree['right'] != None:
        tree['left'] = delLeaves(tree['left'])
        tree['right'] = delLeaves(tree['right'])
        return tree
#########################
def BSTlist(BST):
    if BST == None:
        return []
    else:
        lst = BSTlist(BST['left']) + [BST['data']] + BSTlist(BST['right'])
        return lst
#########################
def removeMin(tree, val):
    if tree == None:
        return None
    if tree['data'] == val:
        if tree['left'] != None:
            tree['left'] = None
    elif tree['data'] > val:
        tree['left'] = removeMin(tree['left'], val)
    elif tree['data'] < val:
        tree = removeMin(tree['right'],val)
    return tree
#########################
def negate(tree):
    if tree == None:
        return None
    elif tree['left'] == None and tree['right'] == None:
        tree['data'] = tree['data']*(-1)
        return tree
    else:
        tree['data'] = tree['data']*-1
        tree['left'] = negate(tree['left'])
        tree['right'] = negate(tree['right'])

        tree['left'], tree['right'] = tree['right'],tree['left']
        return tree
#########################
def sumBST(BST):
    sums = 0
    if BST == None:
        return 0
    else:
        sums = BST['data']
        sums += sumBST(BST['right'])
        sums += sumBST(BST['left'])
    return sums
#########################
def newDel(BST, value):
    if tree == None:
        return None
    elif value < tree['data']:
        tree['left'] = delete(tree['left'],value)
        return tree
    elif value > tree['data']:
        tree['right'] = delete(tree['right'],value)
        return tree
    else: # root note contains value
        if tree['left'] == None:
            return tree['right']
        elif tree['right'] == None:
            return tree['left']
        else:
            nextRoot = greatestNode(tree['left'])
            tree['data'] = nextRoot['data']
            tree['left'] = delete(tree['left'], nextRoot['data'])
            return tree

#########################
def delete(tree, value):
    """
    Delete value from tree and return pointer to the root of the
    modified tree.  (This will be different from the original root
    only when deleting the value at the root.)
    If the value is not in the tree, does not change the tree.
    """
    if tree == None:
        return None
    elif value < tree['data']:
        tree['left'] = delete(tree['left'],value)
        return tree
    elif value > tree['data']:
        tree['right'] = delete(tree['right'],value)
        return tree
    else: # root note contains value
        if tree['left'] == None:
            return tree['right']
        elif tree['right'] == None:
            return tree['left']
        else:
            # This is the messy case: the node to delete has
            # two children.
            # Find the smallest value in the right subtree.
            # (The largest value in the left subtree would work
            # equally well.)
            nextRoot = smallestNode(tree['right'])
            tree['data'] = nextRoot['data']
            tree['right'] = delete(tree['right'], nextRoot['data'])
            return tree
        
#########################
def combDel(tree, value):
    if tree == None:
        return None
    elif value < tree['data']:
        tree['left'] = delete(tree['left'], value)
        return tree
    elif value > tree['data']:
        tree['right'] = delete(tree['right'], value)
        return tree
    else:
        x = rand.randint(1,2)
        if x == 1: # delete greatest value in left subtree
            nextRoot = greatestNode(tree['left'])
            tree['data'] = nextRoot['data']
            tree['left'] = delete(tree['left'], nextRoot['data'])
            return tree
        elif x == 2: # delete smallest value in right subtree
            nextRoot = smallestNode(tree['right'])
            tree['data'] = nextRoot['data']
            tree['right'] = delete(tree['right'], nextRoot['data'])
            return tree
            
        
#########################
def smallestNode(tree): # assume tree won't be empty
    """
    Returns the smallest node in a tree
    """    
    if tree['left'] == None:
        return tree
    else:
        return smallestNode(tree['left'])
#########################
def greatestNode(tree):
    if tree['right'] == None:
        return tree
    else:
        return greatestNode(tree['right'])
    
import random
def randomTree(size, echo=False):
    """
    For testing: create a tree containing random integers.
    """
    tree = None
    for i in range(size):
        x = random.randint(1,100)
        if echo:
            print x
        tree = add(tree,x)
    return tree

def printTree(tree, indent=0):
    """
    Recursive version is simple: print the right sub-tree, the root,
    and the left subtree.  (In that order so that if you tilt your head
    to the left things are in the right place.)
    Second parameter is the amount to indent the tree.
    """
    if tree == None:
        return
    else:
        printTree(tree['right'],indent+4)
        print " "*indent + str(tree['data'])
        printTree(tree['left'],indent+4)

def add(tree, value):
    """
    Add value to tree and return pointer to the root of the modified
    tree.  (This will be different from the original root only when
    we're adding the value to an empty tree.)
    """

    # If the tree is empty, this value becomes the new root.
    # Otherwise, recursively add the value to the left or right
    # sub-tree.
    if tree == None:
        return {'data':value, 'left':None, 'right':None}
    elif value <= tree['data']:
        tree['left'] = add(tree['left'],value)
        return tree
    else: # value > tree['data']
        tree['right'] = add(tree['right'],value)
        return tree
#########################
def leafCount(tree):
    sums = 0
    if tree == None:
        return 0
    else:
        sums += leafCount(tree['left'])
        sums += leafCount(tree['right'])
    return sums

#########################
def leafCount2(tree):
    sums = 0
    if tree == None:
        return 0
    elif tree['left'] != None or tree['right'] != None:
        sums += leafCount2(tree['left'])
        sums += leafCount2(tree['right'])
        return sums
    else:
        return 1
#########################
def deleteMin(tree):
    if tree == None:
        return None
    elif tree['left'] != None:
        tree['left'] = deleteMin(tree['left'])
        return tree
    elif tree['right'] != None:
        tree = tree['right']
        return tree
#########################
def countOdd(tree):
    if tree == None:
        return 0
    else:
        leftOdd = countOdd(tree['left'])
        rightOdd = countOdd(tree['right'])
        odd = leftOdd + rightOdd
        if tree['data']%2 != 0:
            odd +=1
        return odd
