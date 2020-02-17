# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # Find the lowest element, and switch places 
    # loop through n-1 elements
    for i in range(len(arr)-1):
        cur_index  = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = ar[cur_index], arr[smallest_index]

        print(arr)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
