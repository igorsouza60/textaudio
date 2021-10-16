import pyttsx3

engine = pyttsx3.init()
f = open("text.txt", "r", encoding="utf-8").read()

volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.save_to_file(f, "audio.mp3")
engine.runAndWait()