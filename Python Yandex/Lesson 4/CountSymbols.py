def main ():
    pass 
class CountError(Exception):
    pass    
def count_symbols(filename,line_index):
    try: 
        with open(filename) as f:
             current =0
             for line in f:
                if current==line_index:
                    return len(line)-1
                current+=1
        raise CountError("Line with index"+str(line_index)\
        +"not found")
    except IOError:
        raise CountError("File not found")                