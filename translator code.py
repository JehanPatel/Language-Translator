from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests, uuid, json
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="b62e765434e44689b2c1f9ac3958b6f9", region="eastasia")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)


speech_config.speech_synthesis_voice_name='hi-IN-MadhurNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

root = tk.Tk ()
root.title("Microsoft Language Translator")
root.geometry('590x370')

frame1 = Frame(root, width=590, height=370, relief = RIDGE, borderwidth = 5, bg='#F7DC6F')
frame1.place(x=0,y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)

def translate():
  lang_1 = text_entry1.get("1.0", "end")
  text_entry2.delete(1.0 , "end")
  cl=choose_language.get()
  try:
    for (key,value) in LANGUAGES.items() :
      if (value==cl):
        lang_key = key   
    
    key = "17930e6220fc4603a5edf1df60745686"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    location = "eastasia"
    
    path = '/translate'
    constructed_url = endpoint + path
    
    params = {
        'api-version': '3.0',
        'to': [lang_key],
    }
    
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    body = [{
        'text': lang_1
    }]
    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    text_entry2.insert('end', response[0]["translations"][0]['text'])
    speech_synthesis_result = speech_synthesizer.speak_text_async(response[0]["translations"][0]['text']).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(response[0]["translations"][0]['text']))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

  except Exception as e :
    messagebox.showerror(e)


def clear():
	text_entry1.delete(1.0,'end')
	text_entry2.delete(1.0, 'end')

a = tk.StringVar()


auto_select = ttk.Combobox(frame1, width=27, textvariable=a, state='randomly', font =('verdana', 10, 'bold'))
auto_select['values'] = (
	'Auto'
)

auto_select.place(x=15, y=60)
auto_select.current(0) 

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state='randomly', font=('verdana',10, 'bold'))

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}
def speak():
    speech_config = speechsdk.SpeechConfig(subscription="b62e765434e44689b2c1f9ac3958b6f9", region="eastasia")
    speech_config.speech_recognition_language="en-IN"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text_entry1.insert("end" , speech_recognition_result.text)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")


choose_language['values'] = list(LANGUAGES.values())
choose_language.place(x=305,y=60)	
choose_language.current(0)


text_entry1 = Text (frame1, width=20,height=7,borderwidth=5,relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10,y=100)

text_entry2 = Text (frame1, width=20,height=7,borderwidth=5,relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300,y=100)

btn1 = Button(frame1, command = translate, text="Translate", relief=RAISED, borderwidth=2, font=('verdana',10,'bold'), bg='#248aa2', fg="white", cursor="hand2")
btn1.place(x=150, y=300)

btn2 = Button(frame1, command = clear, text="Clear", relief=RAISED, borderwidth=2, font=('verdana',10,'bold'), bg='#248aa2', fg="white", cursor="hand2")
btn2.place(x=270,y=300)

btn3 = Button(frame1, command = speak, text="Speak Something", relief=RAISED, borderwidth=2, font=('verdana',10,'bold'), bg='#248aa2', fg="white", cursor="hand2")
btn3.place(x=350,y=300)



root.mainloop()
