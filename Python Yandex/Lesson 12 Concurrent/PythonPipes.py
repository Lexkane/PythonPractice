import os
import subprocess
from subprocess import check_output, PIPE, Popen


def main():
    pass


p1 = Popen(['echo', 'qwerty'], stdout=PIPE)
p2 = Popen(['tr', 'q', 'z'], stdin=p1.stdout, stdout=PIPE)

p1.stdout.close()
print(p2.communicate)
