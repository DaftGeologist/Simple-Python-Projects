for y in range(5,-6,-1):
    x=y**2
    plot = "*"
    space=" " * (x)
    if x > 0:
        print("%2d|%s%s" % (y,space,plot))
    else:
        print("%2d|%s" % (y,plot))
    
