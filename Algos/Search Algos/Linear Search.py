def linear_search(lst, match):
    for idx in range(len(lst)):
        if lst[idx] == match:
            return idx
        else:
            return ValueError

def find_maximum(lst):
    max = None
    for el in lst:
        if max == None or el>max:
            max = el
    return max


def lin_search_multi(lst, match):
    matches = []
    for idx in range(len(lst)):
        if lst[idx] == match:
            matches.append(idx)
    if matches:
        return matches
    else:
        raise ValueError("{0} not in list".format(match))