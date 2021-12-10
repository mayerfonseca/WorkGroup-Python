class  Analitycs:

    @classmethod
    def media(cls, datos):
        promedio=0.0
        for dato in datos:
            promedio+=dato
        return (promedio/len(datos))

    @classmethod
    def moda(cls,datos):
        frecuencia = {}
        for dato in datos:
            frecuencia[dato] = frecuencia.get(dato, 0) + 1

        mayorfrecuencia = max(frecuencia.values())

        moda = [key for key, value in frecuencia.items()
                 if value == mayorfrecuencia]
        if(len(moda)>1):
            moda="No hay moda"

        return moda

    @classmethod
    def mediana(cls,datos):
        datos.sort()
        mediana=0
        if(len(datos)%2==0):
            mediana = (datos[len(datos) - 1]+datos[len(datos)])/2
        else:
            mediana=datos[len(datos)-1]
        return mediana

    @classmethod
    def minimo(cls,datos):
        minimo=datos[0]
        for dato in datos:
            if(dato<minimo):
                minimo=dato
        return minimo

    @classmethod
    def maximo(cls, datos):
        maximo = datos[0]
        for dato in datos:
            if (dato < maximo):
                maximo = dato
        return maximo
