def decorator(functon_to_decorate):
    def wrapper(chiselki):
        n = function_to_decorate(chiselki)
        if n == 0:
            print('Нет(')
        elif n > 10:
            print('Очень много')
        else:
            print(n)
    return wrapper


@decorator
def F(chiselki):
    n = 0
    for i in chiselki:
        if i % 2 == 0:
            n += 1
    return n