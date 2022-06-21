# text-to-voice-telegram-bot
import telebot
import pyttsx3
from gtts import gTTS


bot = telebot.TeleBot("token")
@bot.message_handler(commands=['start'])
def send_welcome(message):
   bot.send_message(message.chat.id, "Send me a text and I'll turn it into a voice")
   
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    engine = pyttsx3.init()
    theText= message.text
    engine.runAndWait()
    tts = gTTS(text=theText, lang="ru")
    tts.save("file.mp3")
    voice = open('file.mp3', 'rb')
    bot.send_voice(message.chat.id, voice)
        
bot.infinity_polling()  
