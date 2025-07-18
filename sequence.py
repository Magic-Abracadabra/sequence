def seqseg(seq):
'''# Sequence
## Obtaining sequence segments
Example:
```python
from sequence import seqseg
print(seqseg([7,3,6,9,3]))
```
Output:
```plaintext
(([7, 3, 6, 9, 3],), ([7], [3, 6, 9, 3]), ([7, 3], [6, 9, 3]), ([7, 3, 6], [9, 3]), ([7, 3, 6, 9], [3]), ([7], [3], [6, 9, 3]), ([7], [3, 6], [9, 3]), ([7], [3, 6, 9], [3]), ([7, 3], [6], [9, 3]), ([7, 3], [6, 9], [3]), ([7, 3, 6], [9], [3]), ([7], [3], [6], [9, 3]), ([7], [3], [6, 9], [3]), ([7], [3, 6], [9], [3]), ([7, 3], [6], [9], [3]), ([7], [3], [6], [9], [3]))
```'''
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
'''# Sequence
## Is it a sublist of this?
Example:
```python
from sequence import issublist
if issublist([1,2], [1,2,3]):
        print('Sublist')
else:
        print('No')
```
Output:
```plaintext
Sublist
```

 '''
	i = len(near)
	j = near[0]
	if j not in far:
		return None
	else:
		for k in range(far.count(j)):
			if near == far[far.index(j, k): far.index(j, k)+i]:
				return far.index(j, k), i
