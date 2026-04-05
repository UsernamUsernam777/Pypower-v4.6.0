
def minus_clock(time_str1, time_str2):
    """convert time to type_output"""
    t1 = reverse_many_hms(time_str1)
    t2 = reverse_many_hms(time_str2)
    return how_many_hms_in_s(abs(t1-t2))
def how_many_hms_in_s(sec):
    """how many hours, minutes and seconds in seconds"""
    hours = int(sec // 3600)
    minutes = int((sec % 3600) // 60)
    seconds = int((sec % 3600) % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"
def reverse_many_hms(time_str):
    result = tuple(map(int, time_str.split(':')))
    return (result[0]*3600) + (result[1]*60) + result[2]
