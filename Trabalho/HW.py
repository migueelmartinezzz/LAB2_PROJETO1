def cumprimento(texto):
    return f"Olá {texto}"
print(cumprimento("Miguel Silva Martinez"))
import random

def calcular_media_3numeros():
    # Sortear 3 números aleatórios entre 1 e 100
    numeros = [random.randint(1, 100) for _ in range(3)]
    # Calculando a média dos números
    media = sum(numeros) / len(numeros)
    return media
                  
