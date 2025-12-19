import re

def construir_expresion_regular():
    """
    Genera la Expresión Regular Global corregida para PROHIBIR
    dos puntos seguidos (..) o separadores consecutivos.
    """
    
    tlds_aceptados = [
        "ca", "car", "cars", "care", "cat", "co", "com", "cool", "coop",
        "ne", "net", "new", "news",
        "pa", "pay", "pr", "pro", "prof", "promo", "pics",
        "be", "bet", "beer", "bi", "bid", "biz",
        "se", "sex", "sexy", "so"
    ]
    
    tlds_ordenados = sorted(tlds_aceptados, key=len, reverse=True)
    patron_tlds = "|".join(tlds_ordenados)
    
    # --- CONSTRUCCIÓN DEL PATRÓN REGEX (BLINDADO) ---
    regex = (
        r"^[a-zA-Z0-9]+"            # 1. Empieza obligatoriamente con letras/números
        r"([._-][a-zA-Z0-9]+)*"     # 2. Bucle: (Un solo separador + letras/numeros)
                                    #    Esto impide ".." porque exige texto después del punto.
        r"@"                        # 3. Arroba
        r"[a-zA-Z0-9]+"             # 4. Empieza dominio
        r"([.-][a-zA-Z0-9]+)*"      # 5. Bucle dominio
        rf"\.({patron_tlds})$"      # 6. TLD
    )
    
    return regex

def validar_correo(direccion_correo):
    patron = construir_expresion_regular()
    if re.match(patron, direccion_correo, flags=re.IGNORECASE):
        return "Válida"
    else:
        return "Inválida"

# --- PRUEBAS ---
def ejecutar_bateria_pruebas():
    vectores_prueba = [
        # VÁLIDOS
        "nombre.apellido@empresa.com",
        "a.b.c@test.net",
        
        # INVÁLIDOS (ESTOS SON LOS IMPORTANTES)
        "nombre..apellido@empresa.com",    # Fallará (Correcto)
        "admin@dominio..com",              # Fallará (Correcto)
        ".usuario@dominio.com"             # Fallará (Correcto)
    ]

    print(f"{'DIRECCIÓN DE CORREO':<40} | {'ESTADO'}")
    print("-" * 55)
    
    for correo in vectores_prueba:
        resultado = validar_correo(correo)
        print(f"{correo:<40} | {resultado}")

if __name__ == "__main__":
    print("=== VALIDACIÓN ESTRICTA (SIN PUNTOS CONSECUTIVOS) ===\n")
    ejecutar_bateria_pruebas()