class Elipse:

    @staticmethod
    def simetria(x, y, centro):
         points  = []
         points.append((x + centro[0], y + centro[1]))
         points.append((-x + centro[0], y + centro[1]))
         points.append((x + centro[0], -y + centro[1]))
         points.append((-x + centro[0], -y + centro[1]))

         return points

    @staticmethod
    def midPointElipse(a, b, centro):
        pontos = []
        x = 0
        y = b
        d1 = b*b-a*a*b+a*a/4
        pontos.extend(Elipse.simetria(x, y, centro))
        while(a*a*(y-0.5)>b*b*(x+1)):
            if(d1<0):
                d1 += b*b*(2*x+3)
                x +=1
            else:
                d1 += b*b*(2*x+3)+a*a*(-2*y+2)
                x += 1
                y -= 1
            pontos.extend(Elipse.simetria(x, y, centro))
        
        d2 = b**2*(x+0.5)**2 + a**2*(y-1)**2 - a**2*b**2
        while(y > 0):
            if(d2 < 0):
                d2 += b*b*(2*x+2) + a*a*(-2*y+3)
                x+= 1
                y-=1
            else:
                d2 += a*a*(-2*y+3)
                y-= 1
            pontos.extend(Elipse.simetria(x, y, centro))
        return pontos


    
