from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    if (x0 > x1):
        temp = x1
        x1 = x0
        x0 = temp
        temp = y1
        y1 = y0
        y0 = temp

    A = y1 - y0
    B = -1 * (x1 - x0)
    X = x0
    Y = y0

    #undefined slope
    if (B == 0):
        if (y0 < y1):
            while (Y <= y1) :
                plot(screen, color, X, Y)
                Y += 1
        else:
            while (Y >= y1) :
                plot(screen, color, X, Y)
                Y -= 1
        return

    slope = A * 1.0 / -B

    #OCTANT 1
    if (slope <= 1 and slope >= 0):
        d = 2 * A + B        
        while (X <= x1) :
            plot(screen, color, X, Y)
            if d > 0:
                Y += 1
                d += (2 * B)
            X += 1
            d += (2* A)
    #OCTANT 8
    elif (slope >= -1 and slope < 0):
        d = (2 * A) - B
        while (X <= x1) :
            plot(screen, color, X, Y)
            if d < 0:
                Y -= 1
                d -= (2 * B)
            X += 1
            d += (2 * A)

    #OCTANT 2
    elif (slope > 1):
        d = A + (B * 2)
        while (Y <= y1) :
            plot(screen, color, X, Y)
            if d < 0:
                X += 1
                d += (2 * A)
            Y += 1
            d += (2 * B)
    #OCTANT 7
    elif (slope < -1):
        d =  A - (2 * B)
        while (Y >= y1) :
            plot(screen, color, X, Y)
            if d > 0:
                X += 1
                d += (2 * A)
            Y -= 1
            d -= (2 * B)
    else:
        print "bro"

                
'''
'''
