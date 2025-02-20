def input_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El campo no puede estar vacío.")

def input_numero(mensaje, min_val=0, max_val=100):
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            print(f"Error: El número debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Ingrese un número válido.")

