#Implemente una clase “factura” que tenga un importe correspondiente al total de la factura pero de acuerdo
# a la condición impositiva del cliente (IVA Responsable, IVA No Inscripto, IVA Exento) genere facturas que
#indiquen tal condición. 
from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"
        return result

class IVA_responsableCreator(Creator):
    def factory_method(self) -> Product:
        return FacturaIVAR()

class IVA_noinscriptoCreator(Creator):
    def factory_method(self) -> Product:
        return FacturaIVANI()

class IVA_exentoCreator(Creator):
    def factory_method(self) -> Product:
        return FacturaIVAE()

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class FacturaIVAR(Product):
    def operation(self) -> str:
        return "{Factura para IVA Responsable}"

class FacturaIVANI(Product):
    def operation(self) -> str:
        return "{Factura IVA No Inscripto}"

class FacturaIVAE(Product):
    def operation(self) -> str:
        return "{Factura IVA Exento}"

def client_code(creator: Creator) -> None:
    print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("\n\n")
    print("Creando una Factura para IVA Responsable")
    client_code(IVA_responsableCreator())
    print("\n")

    print("Creando una Factura IVA No Inscripto")
    client_code(IVA_noinscriptoCreator())
    print("\n")

    print("Creando una Factura IVA Exento")
    client_code(IVA_exentoCreator())
