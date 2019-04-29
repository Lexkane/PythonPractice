import tempfile
import shutil

def main():
	pass

@contextmanager
def tempdir():
		outdir=tempfile.mkdtemp()
		try:
			yield outdir
		finally:
			shutil.rmtree(outdir)

with tempdir() as path:
				print(path)