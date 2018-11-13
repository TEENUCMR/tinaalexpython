import speech_recognition as sr

AUDIO_FILE=("example.wav")

r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:



	audio=r.record(source)

try:
	print("THE AUDIO FILE CONTAINS:" +r.recognize_google(audio))

except sr.UnkownValueError:
	print("GOOGLE SPEECH RECOGNITION COULD NOT UNDERSTAND AUDIO")

except sr.RequestError as e:
	print("COULD NOT REQUEST RESULT FROM GOOGLE RECOGNITION SERVICE;{0}".forma)