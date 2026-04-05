
def opponents(iterable, obj):
    """takes iterable for 2 elements and if the obj == anyone, the function returns the other one"""
    if obj == iterable[0]:
        return iterable[1]
    elif obj == iterable[1]:
        return iterable[0]
    return obj

def flat_list(lst, type_to_flat=(list, set)):
    result = []
    for i in lst:
        if isinstance(i, type_to_flat):
            result.extend(flat_list(list(i)))
        else:
            result.append(i)
    return result

def search_iterable(iterable, search_with, ignore_case=True):
    result = []
    for o in iterable:
        if ignore_case:
            if str(search_with).lower() in str(o).lower():
                result.append(o)
        else:
            if str(search_with) in str(o):
                result.append(o)
    return result

def numred(iterable):
    """numred the objects in an iterable ex: if you want to create numred tasks
        numred(['visiting my uncle', 'water the plants'])  1.visiting my uncle"""
    result = ''
    for i in range(len(iterable)):
        result += f"{i+1}. {iterable[i]}\n"
    return result.strip()

def indexes(iterable, obj):
    return [i for i in range(len(iterable)) if iterable[i] == obj]

def replace_iterable(iterable, obj, new_obj=None):
    """replace an object by it's index with new_obj ex:    replace(['mike', 'mark'], 1, 'Olivia')
result = ['Olivia', 'mark']"""
    co = iterable.copy()
    i = indexes(iterable, obj)
    for o in i:
        co.pop(o)
        if new_obj:
            co.insert(o, new_obj)
    return co
def all_any_in(main_iterable, iterable, any_all=all):
    """Checks if all unique elements of 'iterable' exist within 'main_iterable'."""
    if any_all == any:
        for i in set(iterable):
            if i in set(main_iterable):
                return True
    else:
        return set(iterable).issubset(set(main_iterable))

class Dict:
    def multy_key(dic):
        result = {}
        values = set(dic.values())
        for i in values:
            keys = [o for o in dic if dic[o] == i]
            result[str(keys)] = i
        return result
    def swap_dict(dic):
        """k: v ➡ v, k"""
        result = {}
        for k, v in dic.items():
            if isinstance(v, (list, tuple, set, dict)):
                v = str(v)
            result[v] = k
        return result
    def return_dict_in_lines(dec):
        """Return a dict formatted as 'key: value' lines."""
        result = ''
        for i in dec:
            result += f"{i}: {dec[i]}\n"
        return result.strip()
