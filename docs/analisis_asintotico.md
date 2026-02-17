# Análisis de Complejidad Asintótica - Sucesión de Fibonacci en MT

Este documento detalla el análisis teórico de la complejidad temporal y espacial de la Máquina de Turing implementada para calcular la sucesión de Fibonacci.

## 1. Representación y Modelo

- **Modelo**: Máquina de Turing Determinista de una cinta.
- **Entrada**: $n$ en representación unaria (cadena de $n$ unos).
- **Salida**: $F(n)$ en representación unaria.
- **Alfabeto**: $\Sigma = \{1\}$, $\Gamma = \{1, 0, X, Y, \_\}$.

## 2. Complejidad Temporal (Time Complexity)

La complejidad temporal se define como el número de pasos que realiza la máquina en función del tamaño de la entrada $n$.

### Casos Base ($n \le 2$)
Para los casos iniciales, la máquina realiza una cantidad de pasos constante o lineal:
- **$F(0)$**: 1 paso.
- **$F(1)$**: 2-3 pasos.
- **$F(2)$**: 33 pasos.
- Complejidad: $O(n)$

### Caso General ($n > 2$)
En nuestra implementación iterativa, el cálculo de $F(n)$ requiere:
1. Mantener dos valores previos $F(i-1)$ y $F(i-2)$.
2. Sumarlos para obtener $F(i)$.
3. Repetir el proceso $n-2$ veces.

En nuestra MT de una cinta, la suma unaria implica mover la cabeza de lectura/escritura a traves de toda la cinta para copiar simbolos:
- El tamano del numero de Fibonacci $F(n)$ crece de forma exponencial: $F(n) \approx \frac{\phi^n}{\sqrt{5}}$, donde $\phi \approx 1.618$.
- En representacion unaria, el numero de simbolos en la cinta es proporcional al valor de $F(n)$.
- Phase A (b = a + b) requiere recorrer la cinta $O(F(i))$ veces por cada 1 de a.
- Phase B (a = a + b) requiere shift-right de toda la cinta por cada 1 de b, con costo $O(F(i))$ por shift.

Por lo tanto, la complejidad temporal total está dominada por el crecimiento exponencial de $F(n)$:
$$T(n) = O(n \cdot F(n)) = O(n \cdot \phi^n)$$

Esto clasifica al problema en la clase de complejidad **EXPTIME**.

## 3. Complejidad Espacial (Space Complexity)

La complejidad espacial es la cantidad de celdas de la cinta utilizadas.

- **Cinta de entrada**: $n$ celdas.
- **Cinta de salida**: $F(n)$ celdas.
- **Marcadores auxiliares**: $O(n)$ o $O(F(n))$ según la implementación.

Dado que $F(n)$ crece mucho más rápido que $n$:
$$S(n) = O(F(n)) = O(\phi^n)$$

La complejidad espacial también es **exponencial**.

## 4. Comparación: MT vs. Algoritmos Clásicos

| Modelo | Complejidad Temporal | Complejidad Espacial |
|--------|-----------------------|-----------------------|
| **MT Unaria** | $O(n \cdot \phi^n)$ | $O(\phi^n)$ |
| **Iterativo (Binario)** | $O(n)$ | $O(1)$ o $O(n)$ bits |
| **Recursivo (Ingenuo)** | $O(\phi^n)$ | $O(n)$ stack |

## 5. Conclusión

Aunque la Máquina de Turing es capaz de calcular la sucesión de Fibonacci, la elección de la **representación unaria** y la naturaleza de la **cinta única** resultan en una eficiencia extremadamente baja. Este ejercicio demuestra que, si bien una MT es universalmente computable, la eficiencia depende críticamente de la implementación y representación de datos.
