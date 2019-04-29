def main():
	pass
	
d=dict.fromkeys(["foo","bar"],42)
d.keys()
d.values()
d.items()
len(d.items())
42 in d.values()
d.keys()&{"foo"}	

{v for v in d.values()}

for k in d:
	del d[k]
	
d={"foo":"bar"}
d["foo"]

d.get("boo",42)

if key not in d:
		value=default
	else:
		value=d[value]
		
d={"foo":"bar"}
d.setdefault("foo","???")
d.setdefault("boo",42)
d={}
d.update([("foo","bar")],boo=42)


d={"foo":"bar","boo":42}
d.pop("foo")
d.clear()

g={"a":{"b"},"b":{"c"}}
g["a"]
g["b"].add("a")


from collections import defaultdict
g=defaultdict(set,**{"a":{"b"},"b":{"c"}})
g["c"].add("a")

d=dict([("foo","bar"),("boo",42)])
list(d)


from collections import OrderedDict
d=OrderedDict([("foo","bar"),("boo",42)])

d["boo"]="???"
d["bar"]="???"
list(d)


from collections import Counter
c=Counter(["foo","foo","foo","bar"])
c["foo"]+=1

c.pop("foo")
c["boo"]



c=Counter(foo=4,bar=-1)
list(c.elements())

c.most_common(1)

c.update(["bar"])

c.substract({"foo":2})

c=Counter(foo=4,bar=-1)
c2=Counter(foo=2,bar=2)
print(c1+c2)
print(c1-c2)
print(c1&c2)
print(c1|c2)
