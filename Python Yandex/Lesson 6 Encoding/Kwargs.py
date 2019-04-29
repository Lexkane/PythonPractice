def main():
    pass

def complex(**kwargs):
    print(kwargs)
    return(kwargs['real']+1j*kwargs['imag'])
print (complex(real=1,imag=2,hi=3) )   

kwargs={'real':1,'img':2}
print(complex(**kwargs))
