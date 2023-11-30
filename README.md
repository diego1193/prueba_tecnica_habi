# Pythagorean Triples Finder

Este proyecto contiene un script en Python que encuentra todos los triples pitagóricos (ternas pitagóricas) menores o iguales a un número dado.

## Descripción

Los triples pitagóricos son conjuntos de tres números enteros \(a, b, c\) que cumplen la condición \(a^2 + b^2 = c^2\). Este script está diseñado para identificar todos los triples pitagóricos posibles que no superen un número máximo especificado.

### Funcionamiento

El script define una función `triple_pitagorico(num)` que recibe un número entero `num`. Esta función busca todas las combinaciones posibles de números \(a, b, c\) menores o iguales a `num` que cumplan con la condición pitagórica.

## Ejemplo

Si establecemos el valor de `num` en 10, los triples pitagóricos encontrados serán:

- (3, 4, 5)
- (4, 3, 5)
- (6, 8, 10)
- (8, 6, 10)

## Uso

Para utilizar este script, sigue estos pasos:

1. Clona el repositorio a tu máquina local.
2. Abre tu terminal y navega hasta la carpeta del proyecto.
3. Ejecuta el script utilizando Python 3 con el comando `python3 prueba.py`.

### Resultados

Después de ejecutar el script, verás una salida similar a la siguiente:

```python
[(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
