# sort based on string length in list

# my solution
def sort_by_length(arr):
    arr.sort(key=len)
    return arr


print(sort_by_length(["a", "dog", "food", "of"]))


# ['', 'brains', 'moderately', 'pizza'] should equal ['', 'pizza', 'brains', 'moderately']


# code wars
def sort_by_length(arr):
    return sorted(arr, key=len)
