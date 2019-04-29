 def main():
    pass


def notify_about_calls(func):
    def decorated(*args, **kwargs):
        print("Called", func.__name__)
        return func(*args, **kwargs)
    return decorated

def f(a,b):
    return a+b

g=notify_about_calls(f)
print(g(1,2))   