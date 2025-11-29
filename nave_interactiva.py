# nave_interactiva.py

from pathlib import Path

# Importamos las funciones de voz y escucha
# Ajustá estos nombres según tus scripts reales
from voz_nave import decir
from escuchar_nave import escuchar_una_frase


# --------------------------
# Procesamiento de comandos
# --------------------------

def procesar_comando(texto_original: str) -> str | None:
    """
    Recibe el texto que dijo el usuario y devuelve la respuesta
    que tiene que decir la nave. Si no entiende, devuelve None.
    """
    texto = texto_original.strip().lower()

    # --- SALUDOS ---
    if "hola" in texto or "buenos dias" in texto or "buen día" in texto:
        return "Hola capitán, todos los sistemas están en línea."

    # --- ESTADO DEL SISTEMA ---
    if "estado del sistema" in texto or "como esta el sistema" in texto or "cómo está el sistema" in texto:
        return "Todos los módulos funcionales, sin errores reportados."

    # --- CÓMO ESTÁS ---
    if "como estas" in texto or "cómo estás" in texto:
        return "Funcionando dentro de parámetros normales. Gracias por preguntar."

    # Podés seguir agregando más comandos con 'if "...' in texto'

    # Si no reconoce el comando:
    return None



# --------------------------
# Loop principal de la nave
# --------------------------

def loop_nave():
    """
    Loop principal:
    - Saluda
    - Escucha por micrófono
    - Procesa comandos
    - Responde por voz
    - Sale cuando detecta 'salir'
    """

    decir("Sistema de nave interactiva iniciado. Di salir para terminar.")

    while True:
        # 1) Escuchar al usuario
        print("Esperando comando de voz...")
        frase = escuchar_una_frase()  # debe devolver un string

        if not frase:
            # Si no se reconoció nada, seguimos escuchando
            print("No se reconoció nada, sigo escuchando.")
            continue

        print(f"Tú dijiste: {frase}")
        frase_limpia = frase.strip().lower()

        # 2) Comando para salir
        if "salir" in frase_limpia:
            decir("Cerrando sistema de nave. Hasta luego, capitán.")
            break

        # 3) Procesar comando
        respuesta = procesar_comando(frase)

        if respuesta:
            # Si el comando es conocido → responder
            decir(respuesta)
        else:
            # Si no lo entiende, responde algo neutro
            decir("No reconozco ese comando todavía, capitán.")


if __name__ == "__main__":
    # Opcional: asegurar que estamos en el directorio del script
    base = Path(__file__).parent
    print(f"Iniciando nave_interactiva.py desde {base}")
    loop_nave()