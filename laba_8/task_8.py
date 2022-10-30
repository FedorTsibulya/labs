import itertools

def compress_string(s):
    num_quantity = itertools.groupby(s)
    result = []
    for i in num_quantity:
        result.append((len(list(i[1])), int(i[0])))
    return result


print(compress_string('1222311'))
