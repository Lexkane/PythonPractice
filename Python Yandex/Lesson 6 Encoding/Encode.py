def main():
    pass

with open('in.txt') as fin:
    data_in=fin.read()
text_in =data_in.decode('utf-8')       

data_out=text_out.encode('utf-8')
with open('out.txt','w') as fout:
    fout.write(data_out)