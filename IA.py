import openai
from Config import SECRET_KEY

openai.api_key = SECRET_KEY


def chatIA(user, question):
    user.addConversation('\nHumano: ' + question + '\nAI: ')
    answer = getAnswer(user)
    user.addConversation(answer)
    return answer


def getResponse(user):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user.getConversation(),
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        presence_penalty=0.6,
        stop=['\n', 'Humano: ', 'AI: ']
    )
    return response


def getAnswer(user):
    answer = ''
    while answer == '':
        response = getResponse(user)
        answer = response.choices[0].text.strip()
    return answer
