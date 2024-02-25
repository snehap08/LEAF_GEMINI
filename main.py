from config import key
import requests #web
from mic_input import mic1
print (key)
def chat1(chat):
    messages =[] #list contain all the messages
    system_message = "you are an english trainer, provide feedback on any grammar or spelling errors while conversation with user and suggest new vocabulary to user" #first instruction
    message = {"role": "user", "parts": [{"text": system_message + "\n" + chat}]} 
    messages.append(message)
    data = {"contents":messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)

    t1= response.json()
    # print(t1)
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")  #returning the generated text
    print(t2)

# chat = mic1()
chat = input("Enter the query: ")
# chat = "who is MS Dhoni" #{'candidates': [{'content': {'parts': [{'text':
chat1 (chat)