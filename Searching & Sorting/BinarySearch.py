def binarySearchHelper(lst, elem, left, right):
    # exit condition : when 'left' pointer cross over 'right' pointer
    if left > right:
        return None
    else:
        mid = (left + right) // 2
        if lst[mid] == elem:
            return mid
        elif lst[mid] < elem:
            return binarySearchHelper(lst, elem, mid + 1, right)
        elif lst[mid] > elem:
            return binarySearchHelper(lst, elem, left, mid-1)

def binarySearch(lst, elem):
    res = binarySearchHelper(lst, elem, 0, len(lst)-1)
    if res is None:
        print(f"Element {elem} is not found in the given list")
    else:
        print(f"Element {elem} is found at position {res}")
    return

lst = [1, 3, 6 ,7, 9, 10, 12]

# example-1
binarySearch(lst, 9)
binarySearch(lst, 1)
binarySearch(lst, 20)
