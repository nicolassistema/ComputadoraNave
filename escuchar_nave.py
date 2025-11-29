import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# Ruta al modelo de Vosk (carpeta que descomprimiste)
MODEL_PATH = r"C:\Computadora_nave\modelos\vosk-model-small-es-0.42"

# Cargamos modelo
print("Cargando modelo de voz, espera un momento...")
model = Model(MODEL_PATH)

audio_queue = queue.Queue()
recognizer = None


def callback(indata, frames, time, status):
    """Callback original, simple, sin procesar el audio."""
    if status:
        print(status, flush=True)
    audio_queue.put(bytes(indata))


def _init_recognizer():
    global recognizer
    recognizer = KaldiRecognizer(model, 16000)  # igual que antes


def escuchar_una_frase() -> str:
    """
    Escucha por el micrófono hasta que Vosk detecta una frase completa
    y devuelve el texto reconocido (string).
    Devuelve "" si no reconoce nada.
    """
    _init_recognizer()

    # limpiamos cola
    with audio_queue.mutex:
        audio_queue.queue.clear()

    print("Iniciando escucha de la nave. Habla por el micrófono...")

    texto = ""

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback,
    ):
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                texto = json.loads(result).get("text", "")
                if texto:
                    print(f"[Reconocido]: {texto}")
                    break

    return texto


def escuchar_loop_salir():
    """
    Versión compatible con tu script viejo:
    se queda escuchando hasta que digas 'salir'.
    """
    print("Iniciando escucha de la nave. Habla por el micrófono...")
    _init_recognizer()

    with audio_queue.mutex:
        audio_queue.queue.clear()

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback,
    ):
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                texto = json.loads(result).get("text", "")
                if texto:
                    print(f"[Reconocido]: {texto}")
                    if texto.strip().lower() == "salir":
                        print("Comando 'salir' detectado. Cerrando escucha.")
                        break


if __name__ == "__main__":
    # Prueba como el script viejo:
    escuchar_loop_salir()
