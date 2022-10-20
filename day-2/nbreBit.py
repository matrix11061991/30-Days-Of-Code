def nbrbit(n) :
	"""calculate the number of bits to encode a decimal in binary.
    :param int number: decimal number.
    :returns: decimal number.
    :rtype: string
    """
    return len(list(dectobin(n)))
def dectobin(n):
    resultat = ""
    while n >= 2 :
        resultat =  str(n % 2) + resultat 
        n = n // 2
    resultat =  str(n) + resultat
    return resultat
print(nbrbit(12))