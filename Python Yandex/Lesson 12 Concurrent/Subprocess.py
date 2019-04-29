import os
import subprocess
from subprocess import check_output, PIPE


def main():
    pass


subprocess.check_output(['echo', 'hello,world'])
subprocess.check_output('exit 1', shell=True)

p0 = subprocess.Popen(['echo', 'hi'])
p0.communicate()

p1 = subprocess.Popen(['echo', 'hi'], stdout=subprocess.PIPE)
p1.communicate()


p = subprocess.Popen(['cat'],
                     stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE)
p.communicate('sample text')
