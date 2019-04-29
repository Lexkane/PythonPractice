from threading import Thread
def main():
    pass

threads=[]
for i in range(SIZE):
    t=Thread(target=test,args=(i,inputs,outputs))
    threads.append(t)
for t  in threads:
    t.start()

for t in threads:
    t.join()

class TCalc(Thread):
    def __init__(self):
        super(TCalc,self).__init__()
        self.status="starting.."
    def run(self):
        time.sleep(1)
        self.status='done'

t=TCalc()
t.start()
print (t.status)
t.join()
print (t.status)