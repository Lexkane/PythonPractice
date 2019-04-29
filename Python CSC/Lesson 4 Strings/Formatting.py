import sys
import io


def main():
    pass


"{!s}".format("i am string")
"{!r}".format("i am string")
"{!a}".format("i am string")

"{:~^16}".format("foo bar")
"int:{0:d} hex:{0:x}".format(42)
"oct:{0:o} bin :{0:b}".format(42)
"{:+08.2f}".format(-42.42)

"{!r:~^16}".format("foo bar")

print("Hello,'sys.stdout'!", file=sys.stdout)
print("Hello,'sys.stderr'!", file=sys.stderr)

chunk="i am string".encode("cp1251")
chunk.decode("utf-8","ignore")
chunk.decode("utf-8","replace")

print(*range(4),end="\n--\n")

handle=open("example,txt","w")
print(*range(4),file=handle,flush=True)

handle=io.StringIO("test.txt")
handle.readline()
handle.write("boo")
handle.getvalue()
handle=io.BytesIO(b"foobar")
handle.read(3)
handle.getvalue()

handle=write("abracadabra")
handle.writelines(["foo","bar"])
handle=open("example.txt")
handle.read(16)

handle=open("example.txt")
len(handle.readline())

handle.readline(16)
handle.readlines(hint=16)