# composicion 

" Una coordenada en dos dimenciones esta compuesta por dos valores en el eje de las x y el valor en el eje de las y, esta podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas ue son los cutro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada."

# clse coordenada 

class Coordenada:
    
    # metodo constructor 
    def __init__ (self, x, y):
        self.x = x 
        self.y = y

    # metodo par mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.x, ",", self.y, ")")

# clse cuadro

class Cuadrado:
    
    ## metodo constructor 
    def __init__(self,v1,v2,v3,v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4


    # metodo para mostrar los vertices 
    def mostrarVertices(self):
        print("El cuadrado esta conpuesto por los siguientes vertices: ")
        self.v1.mostrarCoordenada()
        self.v2.mostrarCoordenada()
        self.v3.mostrarCoordenada()
        self.v4.mostrarCoordenada()

# metodo principal
def main():
    # input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    # processing
    c1 = Coordenada(x1,x2)
    c1.mostrarCoordenada()   

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()


if __name__ == "__main__":
    main()