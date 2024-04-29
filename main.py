<<<<<<< HEAD
from User import User
from IA import chatIA

=======
from Telegram import BotTelegram

'''from User import User
from IA import chatIA
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405
user = User(1)
while True:
    question = input('Ingresar: ')
    response = chatIA(user, question)
    print(response)
<<<<<<< HEAD
=======

exit()'''
telegram = BotTelegram()
telegram.run()
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405
