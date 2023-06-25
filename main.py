from User import User
from IA import chatIA

user = User(1)
while True:
    question = input('Ingresar: ')
    response = chatIA(user, question)
    print(response)
