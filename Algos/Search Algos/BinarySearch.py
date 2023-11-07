#recursive implementation
def binary_search(lst, match):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst)//2
        if lst[mid] == match:
            return True
        elif lst[mid] < match:
            return binary_search(lst[mid+1:], match)
        else:
            return binary_search(lst[:mid], match)