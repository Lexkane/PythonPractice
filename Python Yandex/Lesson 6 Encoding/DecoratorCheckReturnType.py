def main():
    pass

def check_return_type(_type):
    def decorator(func):
        def decorated(*args,**kwargs):
            val=func(*args,**kwargs)
            assert isinstance(val,type_)
        return decorated
    return decorator        