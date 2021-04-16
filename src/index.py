from home_menu import HomeMenu
from login import LoginMenu

def main():
    login = LoginMenu()
    username=login.login()
    
    home = HomeMenu(username)
    home.start()

if __name__ == '__main__':
    main()
