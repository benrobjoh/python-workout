def menu(**kwargs):
    name = input('Choose a Callable: ')
    if to_call := kwargs.get(name):
        return to_call()
    else:
        raise ValueError()
