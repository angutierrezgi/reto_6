# reto_6
This repository refers to the activities proposed for class 12 of the Object Oriented Pogramming course.
___
## reto_1 revisitado
Se han creado, las excepciones necesarias, para cada código dentro de los 5 ejercicios básicos creados para el reto 1, se detallará exactamente lo que se ha hecho más adelante.
#### Calculadora básica
* Se creó una clase de excepción llamada *InvalidOperationError* para trabajar con mayor facilidad, el caso default del match-case implementado a la hora de elegir el operador.
* Se utiliza un ciclo *while* para repetir el código siempre que surga un error.
#### Palíndromos
* Se implementó un chequeo de tipo para las palabras en la función palíndromo, mas no es necesario por el hecho de que todo input recibido siempre será tratado primero como *str*.
### Lista de números primos
* Se maneja un chequeo cuando se recibe el número de la cantidad de dígitos a tratar, y se repite si surge un error.
* Se implementa un chequeo similar por cada número ingresado a la lista para ser referido a la función **is_prime**.
#### Suma de números consecutivos
* Se realiza un chequeo, como en el ejercicio anterior.
* Nuevamente, se implementa un chequeo constante por cada dígito ingresado al código funcional.
#### Anagramas
* Se hace búsqueda de palabras en la lista dada, y cualquier ingreso de datos no *str* es ignorado fuera de la funcionalidad del diccionario.
___
## Paquete Shape revisitado
Se hace énfasis en la creación de las subclases con restricciones, siendo específicamente *Square*, garantizando la medida de sus lados, y las clases *Isosceles*, *Equilateral*, *Scalene*, y *TriRectangle*, con sus restricciones en las medidas propias de sus lados y ángulos, haciendo un
```python
raise ValueError(...)
```
específico a cada una de las subclases. Esto mismo puede ser tratado con mayor profundidad a la hora de instanciar estas clases, haciendo un bloque `try`-`except`, cuando se quiera construir a partir de las definiciones y restricciones propias de cada clase.
