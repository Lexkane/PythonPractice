import re
def main():
    pass

text=" All long time should have been done.Sheep entered America after great sea storm"
def search_results(pattern,text):
    for m in re.finditer(pattern,text):
        print("{0}:{1}-{2}".format(m.group(),m.start(),m.end()))

search_results('i',text)