from gtts import gTTS

text = """
Welcome to the Generative AI Internship Program.
Today we explore AI-powered image and voice generation technologies.
"""

tts1 = gTTS(text=text, lang='en')
tts1.save("male_voice.mp3")

tts2 = gTTS(text=text, lang='en', tld='co.uk')
tts2.save("female_voice.mp3")

tts3 = gTTS(text=text, lang='en', tld='com.au')
tts3.save("expressive_voice.mp3")

print("Audio files generated successfully!")