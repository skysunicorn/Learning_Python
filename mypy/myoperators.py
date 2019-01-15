def sqr(x,y=2):
    return x**(1/y)
def parasov(a,b,c):
    dt=b**2-4*a*c
    if dt > 0:
        roots=[(-b+dt**(1/2))/(2*a),(-b-dt**(1/2))/(2*a)]
        print ("x1 = ",roots[0])
        print ("x2 = ",roots[1])
        return(roots)
    elif dt == 0:
        roots=[(-b+dt**(1/2))/(2*a),(-b-dt**(1/2))/(2*a)]
        print ("x1 = x2 = ",roots[0])
        return(roots)
    elif dt < 0:
        roots=[(-b+dt**(1/2))/(2*a),(-b-dt**(1/2))/(2*a)]
        print ("Be Careful! This function has no real roots!")
        print ("x1 = ",roots[0])
        print ("x2 = ",roots[1])
        return(roots)
    else:
        print("Are You Kidding Me???")
