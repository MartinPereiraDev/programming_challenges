def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    numero = abs(int(decimal))
    
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    
    if decimal < 0:
        binario = "-" + binario
    
    return binario

# Solicitar entrada al usuario
numero_decimal =  27  #float(input("Ingrese un numero decimal: "))

# Convertir a binario
numero_binario = decimal_a_binario(numero_decimal)

# Mostrar resultados
print(f"Número decimal: {numero_decimal}")
print(f"Número binario: {numero_binario}")


def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    numero = abs(int(decimal))
    
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    
    if decimal < 0:
        binario = "-" + binario
    
    return binario

# Bucle principal para permitir múltiples conversiones
while True:
    try:
        # Solicitar entrada al usuario
        numero_decimal = 45  #float(input("Ingrese un número decimal (o 'q' para salir): "))
        
        # Convertir a binario
        numero_binario = decimal_a_binario(numero_decimal)

        # Mostrar resultados
        print(f"Número decimal: {numero_decimal}")
        print(f"Número binario: {numero_binario}")
    
    except ValueError:
        print("Error: Por favor, ingrese un número decimal válido.")
    
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        break
    
    print()  # Línea en blanco para separar cada conversión

print("¡Gracias por usar el conversor!")