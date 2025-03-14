# POO_PYTHON

-El paradicma de POO està basado en una abstraccion del mundo real que nos va a permitir desarrollar programas de forma mas cercana a como vemos el mundo,  pensando en objetos que tenemos adelante y en acciones que podemos hacer con ellos.

## Clase 

-una clase es un tipo de dato cuyas variables se llaman objetos o instancias .
-la clase es la definicion del concepto del mundo real y los objetos o instancias son el "propio"
objeto del mundo real.

### Atributos
-Informacion que almacena la clase.

### Metodos
-operaciones que pueden realizar las clases.

## Definicion de una clase en Python

```Python
class NombreClase:

    def _init_(self,variable,variable2):
        self.Atributo1 = valor1
        self.Atributo2 = valor2

    def nombreMetodo(self):
        bloqueCodigo
```
### Componentes 
```class``: palabra reservada en Python para definir una clase.

```NombreClase``: nombre de la clase que quieres crear.

```def``: palabra reservada en Python que se utiliza para definir tanto el constructor de la clase(metodo que se ejecuta la primera ves que usas una clase) como los diferentes metodos que tiene .

```_init```: palabra reservada en Python para definir el metodo constructor de la clase. Es lo primero que se ejecuta cuando crear un objeto de una clase.

```(self, variablex)```: parametro del constructor de la clase . el parametro slef es obligatorio  y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones.

```self,Atributox```: forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```: nombre del metodo de la clase

```(self)```: parametros del metodo. el parametro self es obligatorio y despues tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones.

-cunado defines una clase debes tener en cuenta los siguientes puntos:
-puedes definir tantos atributos como necesites
- puedes definir tantos parametos en el constructor y en los metodos como necesites.

## Composicion
- consiste en la creacion de nuevas clases a partir de otras clases ya existentes que actuan como elementos compositores de la nueva. 
- las clases exixtentes sera atrubutos de la nueva clase.
-En POO la conposicion significa que entra las dos clsases existe una relacion del tipo "tiene un",
- Ejemplo:
- Una coordenada en dos dimenciones esta compuesta por dos valores en el eje de las x y el valor en el eje de las y, esta podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas ue son los cutro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada.