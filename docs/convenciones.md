# Convenciones para la Maquina de Turing - Sucesion de Fibonacci

## Representacion de enteros no negativos en la cinta

Se utiliza **representacion unaria** para codificar los enteros no negativos:

| Numero | Representacion en cinta |
|--------|------------------------|
| 0      | (vacio)                |
| 1      | 1                      |
| 2      | 11                     |
| 3      | 111                    |
| n      | n veces "1"            |

## Alfabeto de la cinta

| Simbolo | Significado                                      |
|---------|--------------------------------------------------|
| `1`     | Digito unario (representa una unidad)            |
| `0`     | Separador entre numeros en la cinta              |
| `_`     | Blanco (celda vacia, delimita el espacio de trabajo) |

## Formato de la cinta

La cinta utiliza `0` como separador entre los numeros representados en unario.

**Ejemplo:** Para calcular F(5), la entrada es `11111` (5 en unario). Al finalizar, la cinta contendra el resultado F(5) = 5 representado como `11111`.

## Interpretacion de la respuesta

- La **entrada** es un numero `n` en unario: se escribe `n` veces el simbolo `1`.
- La **salida** es el valor de F(n) en unario, ubicado en la cinta al finalizar la ejecucion. El resultado se lee como la cantidad de simbolos `1` consecutivos que quedan en la cinta cuando la maquina se detiene en el estado de aceptacion.

## Estados de la maquina

- `q0`: Estado inicial
- `q_accept`: Estado de aceptacion (la maquina se detiene con el resultado en la cinta)
- `q_reject`: Estado de rechazo (entrada invalida)

## Definicion formal

La maquina de Turing se define como la 7-tupla:

**M = (Q, Sigma, Gamma, delta, q0, q_accept, q_reject)**

Donde:
- **Q**: Conjunto finito de estados
- **Sigma**: Alfabeto de entrada = {1}
- **Gamma**: Alfabeto de la cinta = {1, 0, _}
- **delta**: Funcion de transicion Q x Gamma -> Q x Gamma x {L, R}
- **q0**: Estado inicial
- **q_accept**: Estado de aceptacion
- **q_reject**: Estado de rechazo
