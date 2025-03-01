import time

def suma(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
    return resultado

if __name__ == "__main__":
    print("¡Hola! Este es un script de prueba en Python.")
    
    x = 10
    y = 5
    suma(x, y)  # Llamamos a la función suma
    
    print("Esperando 3 segundos...")
    time.sleep(3)
    
    print("Fin del script.")
