import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(f"Índice: {i}")
    print(f"  ID:   {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Lang: {voice.languages}")
    print("-" * 30)