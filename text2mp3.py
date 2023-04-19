# pyinstaller --windowed --paths C:\Windows\System32\downlevel text2mp3.py --onefile --hidden-import ctypes --icon="C:\Users\emo\python\images\text2mp3.ico" text2mp3.spec
# ofuscador https://pyob.oxyry.com/
# atencion enm el fichero espec que genera pyinstale hay que cambiar esta line ay poer esto
#  pathex=['C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\ucrt\\DLLs\\x64'],
# o si ya está cambiado ejecutar directamente: pyinstaller --windowed --onefile --clean tes2mp3.spec
import PySimpleGUI as sg                        # Part 1 - The import
import pyttsx3
import time
#initialize pyttsx3 or create object
bot = pyttsx3.init()

voices = bot.getProperty('voices')
index = 0
lista=[]
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   lista.append(f'{voice.id}')
   index +=1
bot.runAndWait()

voices = bot.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

# changing voice :
voices = bot.getProperty('voices')
# it returns a list of voice available
# in your system
print(voices) # print available voices
# change voice ..
#bot.setProperty('voice', voices[0].id)

#voice_id ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_esES_PabloM"
bot.setProperty('voice', voices[0].id)
# changing rate :
rate = bot.getProperty('rate') # return currrent rate
print(rate) # print rate
# change rate default value 200..
bot.setProperty('rate',160)

# changing volume :
volume = bot.getProperty('volume') # return currrent volume value
print(volume) # print current volume...
# change volume..
bot.setProperty('volume',1)
# Define the window's contents
minValue = 120
maxValue = 200
layout = [
            [sg.Text("Select Rate:")],
            [sg.Spin([i for i in range(minValue, maxValue)],     initial_value=minValue, size=(10, 1), enable_events=True, key='rate')],
            [sg.Text("Select Voice:")], 
            [sg.Listbox(values=lista, select_mode='extended', key='listbox', enable_events=True, size=(110, 6))],
            [sg.Text("Write text:")],     # Part 2 - The Layout
            [sg.Multiline(size=(110, 10),key='-INPUT-')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Play'),sg.Button('Save to mp3'), sg.Button('Exit')],
            ]
      
            

# Create the window
window = sg.Window('Texto 2 mp3 Versión alpha Emo 2022', layout)      # Part 3 - Window Defintion



n=0
while True:

    event, values = window.read()
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
 
    rate=values['rate']
    print(rate)
    bot.setProperty('rate',rate)
    if event=='listbox':
        voz=values['listbox'][0]
        print(voz)
        bot.setProperty('voice', voz)
    
    if event=='Play':
        bot.say(values['-INPUT-'])
        bot.runAndWait()
        bot.stop()
        
    # Output a message to the window
    if event =='Save to mp3':
        
        data = values['-INPUT-']
        
        n=n+1
        fichero="text_to_mp-"+str(n)+".mp3"
        bot.save_to_file(data,fichero)
        bot.runAndWait()
        

        window['-OUTPUT-'].update('Text converted to mp3 saved in:'+fichero)
 

    
# Finish up by removing from the screen
window.close()