from decimal import Decimal
import decimal

class Dato:
    def __init__(self,li,ls,fi,Fi,n):
        self.li = li
        self.ls = ls
        self.mi = round((Decimal(li)+Decimal(ls))/2,2)
        self.fi = fi
        self.fr = round(Decimal(fi)/Decimal(n),2)
        self.Fi = Fi
        self.Fr = 0

    def alinea(self,num):
        num = str(num)
        if len(num)<6:
            num+= " "*(6-len(num))
        return num

    def __str__(self):
        clase = f'[{self.li}-{self.ls})'
        if len(clase)<15:
            clase+= " "*(15-len(clase))
        return f'[valor:{clase} mi:{self.mi} fi:{self.alinea(self.fi)} fr:{self.alinea(self.fr)} Fi:{self.alinea(self.Fi)} Fr:{self.alinea(self.Fr)})'