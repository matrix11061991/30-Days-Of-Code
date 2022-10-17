def addbin2(a,b):
	return addi(a,b) if (isinstance(a,str) and isinstance(b,str)) else None
def addi(a,b):
	a,b,c,r  =  list(map(int,list(a))) , list(map(int,list(b))), False, []
	for i in range(len(a)-1 ,-1,-1):
		r += [int(((a[i] and b[i] and c) or (not(a[i]) and b[i] and not(c)) or (not(a[i]) and not(b[i]) and c) or (a[i] and not(b[i]) and not(c))))]
		c = (a[i] and b[i]) or (b[i] and c) or (a[i] and c)
	return [int(c)] + r
# appel de la fonction
a,b =  "111","100"
print(addbin2(a,b))



