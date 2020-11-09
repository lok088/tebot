import telebot

bot = telebot.TeleBot('1455917534:AAG-3y4K1bIJRD6HlVCPppRO260hTx3v2V0')
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
	if message.text == "Hi":
        	bot.send_message(message.from_user.id, "Hello")
	elif message.text == "Who are you?":
		bot.send_message(message.from_user.id, "I am bot")
	elif message.text == "What is your name?":
		bot.send_message(message.from_user.id, "My name is MyFirstTestBot.")
	elif message.text == "What can you do?":
		bot.send_message(message.from_user.id, "I can answe to few simple questions.")
	else:
		bot.send_message(message.from_user.id, "I do not understand you. Try tape some enother text")
bot.polling(none_stop=True, interval=100000)
