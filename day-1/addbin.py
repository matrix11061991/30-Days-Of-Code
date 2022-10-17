def sombin(a,b):
	return bin(int(a,2) + int(b,2))[2:] if (isinstance(a,str) and isinstance(b,str)) else None

