from gtts import gTTS
from playsound import playsound

# The text you want to convert to speech
text = "Hello! This is a text to speech test in Python."

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file
tts.save("output.mp3")

# Playing the converted file
playsound("output.mp3")
