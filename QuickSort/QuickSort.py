#Read the file as list of integers

NUMLIST_FILENAME = "QuickSort.txt"
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]


# Quick Sort to implement number of Comparisions
def quickSort(tosortArray,start,end):
    counter=0
    if end-start >1:

        swapModeElement(tosortArray)
        #tosortArray[start],tosortArray[end-1]=tosortArray[end-1],tosortArray[start]
        #med = start + (end-start+1)//2 -1


        pivot=partitionArray(tosortArray,start,end)
        counter=end-start-1
        leftcounter=quickSort(tosortArray,start,pivot)
        rightcounter=quickSort(tosortArray,pivot+1,end)
        #return tosortArray
        return counter+leftcounter+rightcounter
    else :
        return 0

# Partition the array by the pivot
def partitionArray(tosortArray,start,end):
    pivot = choosePivot(tosortArray,start)
    i= start+1
    for j in range(start+1,end):
        if tosortArray[j]<pivot:
            tosortArray[i],tosortArray[j]=tosortArray[j],tosortArray[i]
            i=i+1
    tosortArray[i-1],tosortArray[start]= tosortArray[start],tosortArray[i-1]
    return i-1

# Swap Element to consider the mode as pivot
def swapModeElement(tosortArray):
    if(len(tosortArray)%2==0):
        med = len(tosortArray)//2
    else :
        med = len(tosortArray+1)//2

    if(checkModeElement(tosortArray[0],tosortArray[med],tosortArray[len(tosortArray)-1])):
        tosortArray[0],tosortArray[med] = tosortArray[med],tosortArray[0]
    elif(checkModeElement(tosortArray[0],tosortArray[len(tosortArray)-1],tosortArray[med])):
        tosortArray[0],tosortArray[len(tosortArray)-1] = tosortArray[len(tosortArray)-1],tosortArray[0]
    else :
        return

#to check the mode of the trio elements in the list
def checkModeElement(first,mid,last):
    if((first<=mid and mid <= last)or(first>=mid and mid >= last)):
        return True


# Choosing a Pivot- can be randomized too
def choosePivot(tosortArray,start):
    return tosortArray[start]

#arraytoSort = [5, 4, 3, 2, 1]
print(quickSort(numList,0,len(numList)))
