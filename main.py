import telebot
from telebot import types

# আপনার বটের টোকেন ও তথ্য
API_TOKEN = '8268289967:AAHjTiX9FsDZstzJDLyg2wDJwFTfLW1i4l4'
ADMIN_ID = 8002097445
NAGAD_NUMBER = '01850191756'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💰 ব্যালেন্স", "📥 ইনভেস্ট করুন")
    markup.add("📱 হেল্পলাইন")
    bot.send_message(message.chat.id, "স্বাগতম! এই বটটি এখন ২৪ ঘণ্টা অনলাইন থাকবে।", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    if message.text == "💰 ব্যালেন্স":
        bot.send_message(message.chat.id, "আপনার বর্তমান ব্যালেন্স: ০.০০ টাকা।")
    elif message.text == "📥 ইনভেস্ট করুন":
        bot.send_message(message.chat.id, f"নগদ (Personal): {NAGAD_NUMBER}\nটাকা পাঠিয়ে TrxID দিন।")
    elif message.text == "📱 হেল্পলাইন":
        bot.send_message(message.chat.id, "অ্যাডমিন আইডি: @tangelhasan48")

print("বট সফলভাবে চালু হয়েছে...")
bot.polling()
