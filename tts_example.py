from gtts import gTTS
import os

# Text to be spoken
text = "1008"

# Set the language and create the TTS object
tts = gTTS(text=text, lang="en")

# Save the speech to an audio file
tts.save("output.mp3")

# Play the audio file (platform-specific)
if os.name == "posix":  # Linux or macOS
    os.system("mpg123 output.mp3")
elif os.name == "nt":  # Windows
    os.system("start output.mp3")
else:
    print("The current OS is not supported for playback.")

