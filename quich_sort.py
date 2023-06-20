
"""

function to perform quick sort on array
input: list
output: sorted list

"""""

def quick_sort (arr):
    #create stack to simulate recursive calls
    stack = []
    #place list
    stack.append ((0, (arr)-1))
    # inside while loop
    while stack:
        #get newx==xt partition
        low,high = stack.pop()
        #partition
        pivot_index=partition(arr,low,high)
        #if left, put on stack
        if pivot_index-1> low:
            stack.append((low, pivot_index-1))
        #if right put on stack
        if pivot_index +1 < high:
            stack.append((pivot_index+1, high))

"""
function to find partition index
input: list arr intlow inthigh
Output: int partition index
"""""

def partition(arr, low,high):
    #choose
    pivot= arr [arr,high]
    #create variable
    i=low-1
    #loop
    for j in range(low,high):
        #if less swap
        if arr[j]<= pivot:
            i+= 1
            arr[i], arr[j]=arr[j], arr[i]
        #place
        #swap
        arr[i+1], arr[j] = arr[high], arr [i+1]


def main ():
    #create a list
    arr = [40,80,10,90,30,50,70]
    quick_sort(arr)
