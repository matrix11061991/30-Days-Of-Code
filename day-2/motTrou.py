def correspond(mot,mot_a_trous):
	"""Checks if the word can match the missing word.
    :param string text: two character strings.
    :returns: decimal number stored as a string .
    :rtype: string
    """
	r = [i for i in range(len(mot)) if mot[i] != mot_a_trous[i]]
	nb = list(mot_a_trous)
	for i in range(0,len(r)):	
		nb[r[i]] = mot[r[i]]
	nb = "".join(nb)
	return True if mot == nb else False
print(correspond('NSI', '***'))