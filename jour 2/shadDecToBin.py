def shadDectobin(n) :
	"""Convert decimal to binary.
    :param string text: the decimal to convert.
    :return : nombre binaire stocké sous forme de chaîne .
    :rtype: string
    """
    resultat = ""
    while n >= 2 :
        resultat =  str(n % 2) + " " + resultat
        n = n // 2
    resultat =  str(n) + " " + resultat
    return resultat
