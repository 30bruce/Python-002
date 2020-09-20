def my_map(func, iter_params):
    return (func(i) for i in iter_params)


if __name__ == '__main__':
    params = [1, 2]
    print(list(map(lambda x: x*x, params)))
    print(list(my_map(lambda x: x*x, params)))