def binToDecBasedOnShadok(chaine):
    """Convert binary to decimal.
    :param string text: the birary to convert, stored as a string.
    :returns: decimal number stored as a string .
    :rtype: string
    """
    res = 0
    # la chaine doit etre renverse
    for i,j in zip(range(0, len(chaine)),reversed(chaine)):
        res = res + int(j)*2**(i)
    return res