


#Insert the value in arr
arr=[1,2,3,45,4]+[-1]*5
def insert(arr,position,value,n):
    for i in range(n-1,position-1,-1):
        arr[i+1]=arr[i]
    arr[position]=value

    return arr
print(arr)
arr=insert(arr,7,9,5)
print(arr)

arr=insert(arr,6,90,5)
print(arr)


#delete
arr.remove(1)
print(arr)



#Searching
print("_______________________________________________________________________")


def search(arr,low,high,value):
    
    mid=(low+high)//2

    if value== arr[mid]:
        return mid
    
    elif value > arr[mid]:
        return search(arr,mid+1,high,value)
    elif value< arr[mid]:
        return search(arr,low,mid-1,value)
    return 0

arr=[1,2,3,4,5,6]
print(arr)
n=len(arr)

seaching_val=4
result=search(arr,0,n-1,seaching_val)
print(result)

print('- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(arr)

def delete(arr,value):
    postion=search(arr,0,len(arr)-1,value)
    for num in range(postion,len(arr)-1):
        arr[num]=arr[num+1]
    return n-1

n_arr=delete(arr,4)
for num in range(n_arr):
    print(arr[num],end=' ')



print('\n- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')



#selection sort

print('Sorting Before:')
arr_=[5,4,3,2,1]
print(arr_)

for i in range(len(arr_)-1):
    min_id=i
    for j in range(i+1,len(arr_)):
        if arr_[min_id]>arr_[j]:
            min_id=j
    
    arr_[i], arr_[min_id]=arr_[min_id],arr_[i]
print("After soreting:")
for i in range(len(arr_)):
    print(arr_[i],end=" ")



print('\n- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


#Insertion sorting:

arr=[5,1,4,2]
print("Before sorting",arr)
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print("After sorting",arr)

print('\n- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
#Bubble sort

arr=[1,3,2]
print("Before",arr)

n=len(arr)
for i in range(n):
    swap=False
    for j in range(0,n-i-1):
         
         if arr[j]>arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            swap=True

            
    if swap==False:
        break
print("After:",arr)






print('\n- - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

print("Merge Sort:")
arr=[3,1,2,4]
def merge(arr,start,mid,end):
    #subarray
    subarrone=mid-start+1
    subarrtwo=end-mid
    
    #Dummay varaible
    leftArr=[0]*subarrone
    rightArr=[0]*subarrtwo

    #copying the vales
    for i in range(subarrone):
        leftArr[i]=arr[start+i]
    for j in range(subarrtwo):
        rightArr[j]=arr[mid+1+j]
    
    #initlaizing the index
    leftIndex=0
    rightIndex=0
    mergeIndex=start

    #Merge
    while leftIndex < subarrone and rightIndex < subarrtwo:
        if leftArr[leftIndex]<=rightArr[rightIndex]:
            arr[mergeIndex]=leftArr[leftIndex]
            leftIndex+=1

        else:
            arr[mergeIndex]=rightArr[rightIndex]
            rightIndex+=1

        mergeIndex+=1

    #coping the remining values
    while leftIndex <subarrone :
        arr[mergeIndex]=leftArr[leftIndex]
        leftIndex+=1
        mergeIndex+=1

    while rightIndex <subarrtwo:
        arr[mergeIndex]=rightArr[rightIndex]
        rightIndex+=1
        mergeIndex+=1


def mergesort(arr,start,end):
    if start>=end:
        return

    mid=start+(end-start)//2
    mergesort(arr,start,mid)
    mergesort(arr,mid+1,end)
    merge(arr,start,mid,end)

print(arr)
mergesort(arr,0,len(arr)-1)
print(arr)


"---------------------------------------------------------------------------------------------------------------------------"


# Reverse Array
print("Reverse Array")
arr=[1,2,3]
print(arr)
def reverse(arr,start=0,end=len(arr)-1):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
reverse(arr)
print(arr)


"______________________________________________________________________________________________________________________"
print("Problems")
arr=[1,2,3]
print(arr)
def find_second_lagest_element(arr):
    for i in range(1,len(arr)-1):
        sorted(arr)
        if arr[i]!=arr[0]:
            print("Second Lagest element is",arr[i])



