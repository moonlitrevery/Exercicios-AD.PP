import math


def valida_positivo(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argumento inválido ({arg}): todos os números devem ser positivos")
        return func(*args, **kwargs)
    return wrapper

@valida_positivo
def raiz_quadrada(x):
    return math.sqrt(x)

@valida_positivo
def divisao(a, b):
    return a / b
