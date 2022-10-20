def octet(n,y):
	"""function which takes as argument a character string representing a number in binary, and formats it as a block of bytes.
    :param string text: two character strings.
    :returns: decimal number stored as a string .
    :rtype: string
    """
	sep,j,x = " ",y,len(n)
	print(x%y)
	if x%y != 0:
		n = "0"*(y-x%y) + n
	print(len(n))
	L = [(n[i:i+j]) for i in range(0, len(n), j)]
	return sep.join(L)