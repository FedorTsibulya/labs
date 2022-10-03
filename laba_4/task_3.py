def swap_decorator(function_to_swap):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        function_to_swap(*args, **kwargs)
    return wrapper

@swap_decorator
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)