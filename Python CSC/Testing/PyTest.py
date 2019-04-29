import io
import gzip
import sys

def main():
	pass
def test_ook_eval(capsys,monkeypatch):
	handle:ioStringIo("!")
	monkeypatch.setattr(sys,"stdin",handle)
	ook_eval("Ook.Ook!Ook!Ook.")
	output,_err=capsys.readouterr()
	assert output=="!"
	
def test_reader(tmpdir):
	path=tmpdir.join("example.gz")
	path.write("")
	assert isinstance(reader(str(path)),gzip.GzipFile)