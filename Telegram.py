from telegram import Update, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from Config import TOKEN
from User import User
from IA import chatIA


class BotTelegram:
    def __init__(self):
        self.updater = Updater(TOKEN)
        self.dispatcher = self.updater.dispatcher

        ###COMMANDS###
        self.dispatcher.add_handler(CommandHandler('start', self.start))
        ###END COMMANDS###

        ###MESSAGES###
        self.dispatcher.add_handler(MessageHandler(filters=~Filters.command and Filters.text, callback=self.chat))
        ###END MESSAGES###

    def run(self):
        self.updater.start_polling()
        #self.updater.idle()

    def stop(self):
        self.updater.stop()

    @staticmethod
    def start(update: Update, _):
        msg = 'Erudito responde tus preguntas pero puede dar información falsa sobre eventos recientes.'
        update.message.reply_text(msg)


    @staticmethod
    def help(update: Update, _):
        pass

    @staticmethod
    def chat(update: Update, _):
        update.message.reply_chat_action(ChatAction.TYPING)
        userid = update.message.chat.id
        msg = update.message.text

        try:
            user = User.get(userid)
        except AssertionError:
            user = User(userid)
        except Exception as e:
            print(e)

        answer = chatIA(user, msg)
        update.message.reply_text(answer)

