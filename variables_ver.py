numero = 10
decimal = 3.14
texto = "Ola Spyder"


lista_numeros = [1, 2, 3, 4, 5]
tupla_valores = (10, 20, 30)


diccionario = {
    "nome": "Alumno",
    "idade": 20,
    "curso": "ECP"
}


import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])


suma = array_1d + 10
media = np.mean(array_2d)


def cadrado(x):
    return x ** 2

resultado_funcion = cadrado(5)


lista_cadrados = []
for i in range(5):
    lista_cadrados.append(i**2)

print("Código executado correctamente")
