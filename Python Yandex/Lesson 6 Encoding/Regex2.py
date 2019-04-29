import re


def main():
    pass


text = """ In September 1769 she reached New Zealand, the first European
vessel to visit in 127 years"""

m = re.search('(\w+)\s*([0-9]+)', text)

print(m.group(0))
