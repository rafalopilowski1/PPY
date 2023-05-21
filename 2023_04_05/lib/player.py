class Player:

    def __init__(self, nick, e_mail, passwd, points=0):
        self.progress = {}
        self.nick = nick
        self.e_mail = e_mail
        self.passwd = passwd
        self.points = points

    def __str__(self):
        return f"{self.nick},{self.e_mail},{self.points},{self.passwd}"