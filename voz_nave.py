import pyttsx3

engine = pyttsx3.init()

# Elegí el índice que te mostró listar_voces.py
INDICE_VOZ = 3  # cambiá este número por la voz en español que encontraste

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[INDICE_VOZ].id)

# Ajustes estilo nave
engine.setProperty("rate", 145)   # velocidad
engine.setProperty("volume", 0.9) # volumen

def decir(texto: str):
    """Función principal que usa la nave para hablar."""
    print(f"[Nave] {texto}")  # útil cuando no escuchás audio
    engine.say(texto)
    engine.runAndWait()

# Alias opcional para compatibilidad
def hablar(texto: str):
    decir(texto)

if __name__ == "__main__":
    decir("Sistemas de navegación operativos.")
    decir("Advertencia. Fluctuación de energía detectada en el núcleo de curvatura.")
