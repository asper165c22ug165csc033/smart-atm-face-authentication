from gtts import gTTS

def text_to_speech(text, language='en', filename='otp8.mp3'):
    """
    Convert text to speech and save it as an audio file.

    Parameters:
    - text: The text to be converted to speech.
    - language: The language of the text (default is English).
    - filename: The name of the output audio file (default is 'output.mp3').
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    print(f"Audio file saved as: {filename}")

# Example usage:
text_to_speech("52145", language='en', filename='otp/otp8.mp3')
