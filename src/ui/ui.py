import getpass

class UI:
    def __init__(self):
        pass

    def write(self,text):
        print(text)

    def read(self,text):
        return input(text)
    
    def read_password(seft,text):
        return getpass.getpass(text)
        