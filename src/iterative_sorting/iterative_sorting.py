# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for left in range(cur_index+1, len(arr)):
            if arr[left] < arr[smallest_index]:
                smallest_index = left
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for a in range(0, len(arr)-1):
        for b in range(0, len(arr)-a-1):
            if arr[b] > arr[b+1]:
                # swap
                arr[b], arr[b+1] = arr[b+1], arr[b]
    return arr


'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def count_sort(arr, maximum=None):
    # Your code here
    res = []
    min_num = 0
    max_num = 0

    freq = {}

    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        min_num = min(num, min_num)
        max_num = max(num, max_num)
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in range(min_num, max_num+1):
        if num in freq:
            for i in range(freq[num]):
                res.append(num)
    return res
