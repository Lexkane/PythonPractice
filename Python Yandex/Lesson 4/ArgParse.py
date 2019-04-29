import argparse

def count_lines(filename):
    pass


def count_symbols(filename,line_index):
    with open(filename) as f:
        current=0
        for line in f:
            if current==line_index:
                return len(line)-1
            current+=1    
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('filename')
    args=pasrser.parse_args()
    print(count_lines(args.filename))

    parser=argparse.ArgumentParser()
    parser.add_argument('filename',help='name for input file')




if __name__=="main":
    main