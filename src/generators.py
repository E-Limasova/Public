def filter_by_currency (lst, s):
    for i in lst:
        if i["operationAmount"]["currency"]["code"] == s:
            yield i

def transaction_descriptions (lst):
    for i in lst:
        yield i["description"]

def card_number_generator (start, end):
    lst = ["{:016d}".format(i) for i in range(start, end + 1)]
    lst = [i[:4] + " " + i[4:8] + " " + i[8:12] + " " + i[12:] for i in lst]
    return lst
