# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:32:24 2018

@author: eccrawford
"""



def addNode(linkedList, jobId, priority): # adds highest priority to least order
    node = {}
    node['jobId'] = jobId
    node['priority'] = priority
    node['next'] = {}
    if linkedList == {}:
        node['next'] = linkedList
        return node
    elif linkedList['priority'] <= priority: #linkedList['priority'] is the head of the list
        node['next'] = linkedList
        return node
    else:
        previous = linkedList
        current = previous['next']
        if current != {}:
            while current['priority'] > priority:
                previous = current
                current = current['next']
                if current == {}:
                    break
            node['next'] = current
            previous['next'] = node
        else:
            linkedList['next'] = node
        
        return linkedList


def removeNode(linkedList, jobId):
    if linkedList['jobId'] == jobId:
        linkedList = linkedList['next']
        
    else:
        ptr = linkedList
        current = ptr['next']
        while current['jobId'] != jobId and current != {}:
            ptr = current
            current = current['next']
        temp = ptr
        temp['next'] = temp['next']['next']
        ptr = temp
    return linkedList

def details(linkedList, jobId):
    if linkedList['jobId'] == jobId:
        print(linkedList['jobId'], linkedList['priority'])
    else:
        ptr = linkedList
        current = ptr['next']
        while current['jobId'] != jobId and current != {}:
            ptr = current
            current = current['next']
        print(current['jobId'], current['priority'])
        
def show(linkedList):
    ptr = linkedList
    if ptr != {}:
        current = ptr['next']
        countJobs = 0
        priority = 0
        countJobs += 1
        priority = priority + ptr['priority']
        while current != {}:
            ptr = current
            current = current['next']
            countJobs = countJobs + 1
            priority = priority + ptr['priority']
        average = priority/countJobs
        print("The number of jobs currently in the queue is ",countJobs," with average priority", average)
    else:
        print("Time for a coffe break!")


def modifyPriority(linkedList,jobId, newPriority): # change the priority of any job
    #first remove the old node, then readd it with the new priority
    linkedList = removeNode(linkedList, jobId)
    linkedList = addNode(linkedList, jobId, newPriority)
    return linkedList


def respond(linkedList): #remove the first job from the linked list, i.e. the head
    if linkedList != {}:
        print("Responding to job ",linkedList['jobId'])
        linkedList = linkedList['next']
    return linkedList


linkedList = {}
emergencies = open("emergencies.txt", "r")
for line in emergencies:
    job = line.split()
    code = job[0]
    if code == "received":
        jobID = int(job[1])
        priority = int(job[2])
        linkedList = addNode(linkedList, jobID, priority)
        print("added", linkedList)
    if code == "remove":
        jobID = int(job[1])
        linkedList = removeNode(linkedList, jobID)
        print("removed", linkedList)
    if code == "details":
        jobID = int(job[1])
        details(linkedList, jobID)
    if code == "show":
        show(linkedList)
    if code == "respond":
        linkedList = respond(linkedList)
    if code == "modify":
        jobID = int(job[1])
        newPriority = int(job[2])
        linkedList = modifyPriority(linkedList, jobID, newPriority)
