import random

###########################
def is_power(a, b):
    if a == 0 or b == 0:
        return False
    elif a < b:
        return False
    elif a == b or a == 1 or b == 1:
        return True
    else:
        return is_power(a/b, b)

############################
def findMin(numLis):
    if len(numLis) == 1:
        return numLis[0]
    else:
        mini = findMin(numLis[1:])
        if mini < numLis[0]:
            return mini
        else:
            return numLis[0]
#############################
def binSearch(nums, target, lowIndex=0, highIndex=None):
    if highIndex == None:
        highIndex = len(nums)-1
    mid = (lowIndex + highIndex)//2
    if nums[mid] > target:
        return binSearch(nums, target, lowIndex, mid-1)
    elif nums[mid] < target:
        return binSearch(nums, target, mid+1, highIndex)
    else:
        return mid
#############################

def threeMerge(lst):
    if len(lst) < 2:
        return lst
    if len(lst) == 2:
        return lst
    part1 = len(lst) // 3
    part2 = (len(lst) // 3)*2
    
    left = threeMerge(lst[:part1])
    mid = threeMerge(lst[part1:part2])
    right = threeMerge(lst[part2:])
    return merge(left,mid,right)
#############################
def threeQ(lst):
    size = len(lst)
    if size < 2:
        return lst
    else:
        pval1 = lst[0]
        pval2 = lst[1]

        small1 = []
        equal1 = []
        big1 = []
        equal2 = []
        big2 = []

        # less than pval1: small1
        # equal to pval1: equal1
        # greater than p1, less than p2: big1
        # equal to p2: equal2
        # greater than pval2: big2

        for i in range(1,size):
            if lst[i] < pval1:
                small1.append(lst[i])
            elif lst[i] == pval1:
                equal1.append(lst[i])
            elif lst[i] > pval1 and lst[i] < pval2:
                big1.append(lst[i])
            elif lst[i] == pval2:
                equal2.append(lst[i])
            elif lst[i] > pval2:
                big2.append(lst[i])
        return threeQ(small1) + [pval1] + threeQ(equal1) + threeQ(big1) + [pval2] + threeQ(equal2) \
               + threeQ(big2)

#############################
def suesylvestershuffle(lst): #randomly shuffles a list
    if len(lst) == 1:
        return lst
    else:
        newIndex = random.randrange(0, len(lst))
        lst[0], lst[newIndex] = lst[newIndex], lst[0]
        return lst[0:1] + suesylvestershuffle(lst[1:])
#############################
def palindrome(string):
    if len(string) <= 1:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    elif string[0] != string[-1]:
        return False
    else:
        return palindrome(string[1:-1])
#############################
def trace(a,b):
    if (a > b):
        return -1
    elif (a==b):
        print (a*a)
        return a*a
    else:
        m = (a+b) / 2
        return trace(a,m) + trace(m+1,b)
#############################
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
#############################
def sumSquares(m, n):
    if m > n:
        return m**2
    else:
        return m**2 + n**2 + sumSquares(m+1, n-1)
#############################
def printNums(num):
    strnum = str(num)
    if len(strnum) <= 1:
        print(strnum)
    else:
        print(strnum[0])
        return printNums(strnum[1:])

#############################

def numVowels(word):
    vowels = "aeiou"
    if len(word) == 1:
        if word in vowels:
            return 1
        else:
            return 0
    else:
        if word[0] in vowels:
            return 1 + numVowels(word[1:])
        else:
            return 0 + numVowels(word[1:])

#############################

def remVowels(word):
    vowels = "aeiou"
    if len(word) <= 1:
        if word in vowels:
            word = word[1:]
            return word
        else:
            return word
    else:
        if word[0] in vowels:
            word = word[1:]
            return remVowels(word)
        else:
            return word[0] + remVowels(word[1:])

#############################

def multiply(n,m):
    if n > m:
        return None
    if n == m:
        return m
    else:
        mid = (n+m)//2
        return multiply(n,mid) * multiply(mid+1, m)

#############################

def swap(nums):
    if len(nums) < 2:
        return nums
    else:
        return [nums[1],nums[0]] + swap(nums[2:])

#############################

def checkLists(lis1, lis2):
    if len(lis1) != len(lis2):
        return False
    if len(lis1) == 0 and len(lis2) == 0:
        return True
    if lis1[0] == lis2[0]:
        return checkLists(lis1[1:],lis2[1:])
    else:
        return False
