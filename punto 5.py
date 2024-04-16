#Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar para construir 
#aviones en lugar de vehículos. Para simplificar suponga que un avión tiene un “body”, 
#2 turbinas, 2 alas y un tren de aterrizaje.
import os
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getPlane(self):
      plane = Plane()
      
      body = self.__builder.getBody()
      plane.setBody(body)
      
      undercarriage = self.__builder.getUndercarriage()
      plane.setUndercarriage(undercarriage)

      i = 0
      while i < 2:
        turbine = self.__builder.getTurbine()
        plane.attachTurbine(turbine)
        i += 1

      j = 0
      while j < 2:
        wing = self.__builder.getWing()
        plane.attachWing(wing)
        j += 1
      
      return plane

class Plane:
   def __init__(self):
      self.__turbines = list()
      self.__wings = list()
      self.__body = None
      self.__undercarriage = None

   def setBody(self, body):
      self.__body = body

   def attachTurbine(self, turbine):
      self.__turbines.append(turbine)

   def attachWing(self, wing):
      self.__wings.append(wing)

   def setUndercarriage(self, undercarriage):
      self.__undercarriage = undercarriage

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("Alas: %s" % (self.__wings[0].size))
      print ("Tren de aterrizaje: %s" % (self.__undercarriage.time))
      print ("Turbinas: %s" % (self.__turbines[0].size))

class Builder:
	
      def getTurbine(self): pass
      def getWing(self): pass
      def getBody(self): pass
      def getUndercarriage(self): pass

class PlaneBuilder(Builder):
   
   def getTurbine(self):
      turbine = Turbine()
      turbine.size = "300Kw"
      return turbine
   
   def getWing(self):
      wing = Wing()
      wing.size = "80M"
      return wing
   
   def getUndercarriage(self):
      undercarriage = Undercarriage()
      undercarriage.time = "Retractiles"
      return undercarriage
   
   def getBody(self):
      body = Body()
      body.shape = "Boeing 747"
      return body

class Turbine:
   size = None

class Wing:
   size = None

class Undercarriage:
   time = None

class Body:
   shape = None

def main():

   planeBuilder = PlaneBuilder() # initializing the class
   director = Director()

   director.setBuilder(planeBuilder)

   plane = director.getPlane()

   plane.specification()
   print ("\n\n")

if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un Avion\n")

   main()
