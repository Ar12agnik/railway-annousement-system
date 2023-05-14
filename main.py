import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.say('train no 2 2 6 5 2 3 down duttapukur . majerhat local  3 no platform e asche')
engine.runAndWait()
