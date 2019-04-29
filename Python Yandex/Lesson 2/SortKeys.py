import sys

def main():
    
 d={"a":1,"b":5,"c":8}

 for k,v in sorted (d.items(), key=lambda x:x[1]):
  print (k,v)

 name=sys.stdin.read()
 sys.stdout.write(name)

 s="First sentence. 2nd sentence."
 print(s.split(' '))
 print(s.split('.'))
 print(s.rstrip())
 print('a'.isalpha)
 print('a'.isdigit)
  
 print(s.rstrip())
 print(s.strip())


 lines=[]
 for i in range (5):
     lines.append(str(i))
 print('\n'.join(lines))    

if __name__ == "__main__":
    main()
