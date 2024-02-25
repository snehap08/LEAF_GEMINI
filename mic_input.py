import speech_recognition as sr

'''index=0
for name in sr.Microphone.list_microphone_names(): 
    print(index, " : ", name)
    index = index+1'''

recognizer = sr.Recognizer()
def mic1():
    with sr.Microphone(device_index=1) as  source: 
        print("Say  something!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source) # Listen for the user's input.
        print("Recognizing")
        text = recognizer.recognize_google(audio)
        print("you said: ", text)
        return text

if  __name__ == '__main__':
    mic1()