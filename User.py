
class User:

<<<<<<< HEAD
    class Role:
        user = 'user'
        system = 'system'

=======
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405
    users = dict()

    def __init__(self, userid):
        self.userid = userid
<<<<<<< HEAD
        self.conversation = []
=======
        self.conversation = ''
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405
        self.add()

    def add(self):
        if self.userid not in User.users.keys():
            User.users.update({self.userid: self})

    @staticmethod
    def get(userid):
        assert userid in User.users.keys()
        return User.users[userid]

<<<<<<< HEAD
    def addConversation(self, msg, role):
        self.conversation.append({"role": role, "content": msg})
=======
    def addConversation(self, msg):
        self.conversation += msg
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405

    def getConversation(self):
        return self.conversation

    def setConversation(self, conversation):
        self.conversation = conversation
