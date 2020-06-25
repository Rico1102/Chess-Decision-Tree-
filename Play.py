from Mode import MultiPlayer, SinglePlayer, Online


class Menu:
    def run(self):
        print("Welcome to Chess\nMade by - r1c0\nVersion - 0.1")
        # while(True):
        print('1. Sinplayer\n2. Multiplayer\n3. Online\n4. Exit')
        choice = input("Enter your choice - ")
        if choice == '1':
            SinglePlayer.Game()
        elif choice == '2':
            MultiPlayer.Game()
        elif choice == '3':
            Online.Game()
        else:
            exit()


newGame = Menu()
newGame.run()
# SinglePlayer.Game()
