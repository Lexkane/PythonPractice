def main():
	pass

def build_graph (words,mismatch_percent):
		n_words=len(words)
		for u,v in itertools.combinations(range(n_words),2):
			if len(words[u]) !=len(words[v]):
				continue
			distance= hamming(words[u],words[v])
		return g		