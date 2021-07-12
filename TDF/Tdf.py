from decimal import Decimal
from  TDF.Dato import Dato
import math

class Tdf:
    def __init__(self,n,discreta=True):
        self.datos = []
        self.n = n
        self.Fi = 0
        self.Fr = 0
        self.discreta = discreta
        self.cModal = None

    def setDatos(self, ci, fi):
        for index in range(len(fi)):
            self.addDato(ci[index],ci[index+1], fi[index])

    def addDato(self,li,ls,fi):
        Fi = self.Fi + fi
        self.Fi = Fi
        dato = Dato(li,ls,fi,Fi,self.n)
        dato.Fr = Decimal(self.Fr)+Decimal(dato.fr)
        self.Fr = dato.Fr
        self.datos.append(dato)
        if (self.cModal == None or dato.fi > self.cModal.fi):
            self.cModal = dato

    def amplitud(self):
        if(self.discreta):
            return self.datos[0].ls-self.datos[0].li
        else:
            return Decimal(self.datos[0].ls)-Decimal(self.datos[0].li)

    def media(self):
        suma = 0
        for dato in self.datos:
            facto = Decimal(dato.mi)*Decimal(dato.fi)
            suma+= facto
        return round(Decimal(suma)/Decimal(self.n),2)

    def mediana(self):
        maux = self.n//2
        m = None
        ind_1 = -2
        for dato in self.datos:
            ind_1+=1
            if dato.Fi > maux:
                m = dato
                break;
        m_1 = self.datos[ind_1]
        return round(m.li+((maux-m_1.Fi)/(m.fi))*self.amplitud(),2)

    def cuartil(self,h):
        caux = (h*self.n)/4
        c = None
        ind_1 = -2
        for dato in self.datos:
            ind_1+=1
            if dato.Fi > caux:
                c = dato
                break;
        c_1 = self.datos[ind_1]
        return round(c.li+((caux-c_1.Fi)/(c.fi))*self.amplitud(),2)

    def decil(self,h):
        caux = (h*self.n)/10
        c = None
        ind_1 = -2
        for dato in self.datos:
            ind_1+=1
            if dato.Fi > caux:
                c = dato
                break;
        c_1 = self.datos[ind_1]
        return round(c.li+((caux-c_1.Fi)/(c.fi))*self.amplitud(),2)

    def percentil(self,h):
        caux = (h*self.n)/100
        c = None
        ind_1 = -2
        for dato in self.datos:
            ind_1+=1
            if dato.Fi > caux:
                c = dato
                break
        c_1 = self.datos[ind_1]
        return round(c.li+((caux-c_1.Fi)/(c.fi))*self.amplitud(),2)

    def varianza(self):
        media = self.media()
        suma = 0
        for dato in self.datos:
            facto = ((Decimal(dato.mi)-Decimal(media))**2)*dato.fi
            suma+= facto
        return round(suma/self.n,2)

    def desviacionEstandar(self):
        return round(math.sqrt(self.varianza()),2)

    def coeficienteVariacion(self):
        return round((Decimal(self.desviacionEstandar())/Decimal(self.media()))*100,2)

    def asimetriaFisher(self):
        media = self.media()
        suma = 0
        for dato in self.datos:
            facto = ((Decimal(dato.mi)-Decimal(media))**3)*dato.fi
            suma+= facto
        return round(Decimal(suma)/Decimal((self.n*(self.desviacionEstandar()**3))),2)

    def apuntamientoFisher(self):
        media = self.media()
        suma = 0
        for dato in self.datos:
            facto = ((Decimal(dato.mi)-Decimal(media))**4)*dato.fi
            suma+= facto
        return round(Decimal(suma)/Decimal((self.n*(self.desviacionEstandar()**4))),2)

    def printDatos(self):
        indice = 0
        for dato in self.datos:
            print(indice,dato)
            indice+=1
        print(f'\nMedia: {self.media()}')
        print(f'Mediana: {self.mediana()}')
        print(f'Moda: {self.cModal}')
        print(f'Varianza: {self.varianza()}')
        print(f'Desviacion estandar: {self.desviacionEstandar()}')
        print(f'Coeficiente de Variacion: {self.coeficienteVariacion()}')
        print(f'Coeficiente de Asimetria Fisher: {self.asimetriaFisher()}')
        print(f'Coeficiente de Apuntamiento Fisher: {self.apuntamientoFisher()}')