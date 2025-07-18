def seqseg(seq):
	from itertools import combinations as c
	subs = ()
	n_elements = len(seq)
	segs = range(1, n_elements)
	for n_seg in range(n_elements):
		if n_seg==0:
			subs += ((seq, ), )
		else:
			for seg in c(segs, n_seg):
				seg = (0, )+seg+(n_elements,)
				con = ()
				for i, j in enumerate(seg[:-1]):
					con += (seq[seg[i]:seg[i+1]], )
				subs += (con, )
	return subs

def issublist(near, far):
	i = len(near)
	j = near[0]
	if j not in far:
		return None
	else:
		for k in range(far.count(j)):
			if near == far[far.index(j, k): far.index(j, k)+i]:
				return far.index(j, k), i
