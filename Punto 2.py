#Elabore una clase para el cálculo del valor de impuestos a ser utilizado por todas las clases que necesiten realizarlo. 
#El cálculo de impuestos simplificado deberá recibir un valor de importe base imponible y deberá retornar la suma
#del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre esa base imponible.
#SINGLETON
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Impuestos(metaclass=SingletonMeta):
    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        
        total_con_impuestos = iva + iibb + contribuciones
        
        return total_con_impuestos

if __name__ == "__main__":
    calculator1 = Impuestos()
    calculator2 = Impuestos()
    base=int(input("Ingrese el valor: "))

    if id(calculator1) == id(calculator2):
        print("Singleton funciona")
        print("Total a pagar en impuestos: ", calculator1.calcular_impuestos(base))
    else:
        print("Singleton fallo")