
def int_or_float(num):
    try:
        num = str(num).strip()
        float(num)
        assert num[-1] != '.'
        return True
    except:
        return False
def iter_num(iterable):
    """Return sum, average, max, and min of an iterable as a dict."""
    return {'sum': sum(iterable), 'average': sum(iterable) / len(iterable), 'max': max(iterable), 'min': min(iterable)}

def arrays(array, step, show='lists'):
    """Split a range into consecutive [start, end] pairs by step.
    If show != 'lists', return a formatted string instead."""
    result = []
    for i in range(step, array, step):
        result.append([i, i+step])
    if show != 'lists':
        result2 = ''
        for i, e in result:
            result2 += str((i, e)).replace('(', '').replace(')', '').replace(', ', ' - ')+'\n'
        return result2.strip()
    return result
