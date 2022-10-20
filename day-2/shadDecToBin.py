def shadDectobin(n) :
	"""Convert decimal to binary.
    :param string text: the decimal to convert.
    :returns: binary number stored as a string .
    :rtype: string
    """
    resultat = ""
    while n >= 2 :
        resultat =  str(n % 2) + " " + resultat
        n = n // 2
    resultat =  str(n) + " " + resultat
    return resultat