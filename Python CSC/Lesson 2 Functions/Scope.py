def main():
    pass


def cell(value=None):
    def get():
        return value

    def set(update):
        nonlocal value
        value = update
    return get, set


get, set = cell()

mins=0

def f():
    global mins
    mins += 1
    return mins
