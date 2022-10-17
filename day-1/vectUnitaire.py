# Expression du vecteur unitaire n perpendiculaire a la surface d'equation :
# a.x2 + b.y2  + c.z2 = 0, au point P(x,y,z).
def vectUnit(a,b,c,x,y,z):
	# U(x,y,z) = a.x2 + b.y2  + c.z2
	mod = pow((x**2)+(y**2)+(z**2),0.5)
	n = [(2*a*x)/mod,(2*b*y)/mod,(2**z)/mod]
	return n