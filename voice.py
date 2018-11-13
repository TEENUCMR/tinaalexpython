import speech_recognition as sr 

r= sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=5)
	print("SAY SOMETHING")
	while True:#creating while loop
		audio=r.listen(source)#listening to microphone
		print("YOU SAID-" + r.recognize_google(audio))#print ouput

