#Provea una clase que dado un número entero cualquiera retorne el factorial del mismo, 
#debe asegurarse que todas las clases que lo invoquen utilicen la misma instancia de clase.
#SINGLETON
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Factorial(metaclass=SingletonMeta):
    def calculate_factorial(self, n):
        if n == 0 or n == 1:
            return 1
        elif n>1:
            return n * self.calculate_factorial(n - 1)

if __name__ == "__main__":
    calculator1 = Factorial()
    calculator2 = Factorial()

    if id(calculator1) == id(calculator2):
        print("Singleton funciona")
        print("Factorial de 5 es: ", calculator1.calculate_factorial(7))
    else:
        print("Singleton fallo")