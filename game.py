import random

class Game:
    def __init__(self):
        self._board = []
    
    def generateGames(self, gamesTotal, doors = 3):
        for i in range(gamesTotal):
            newgame = [0] * doors
            carpos = random.randint(0,doors-1)
            newgame[carpos] = 1
            goats = [i for i in range(doors) if i != carpos]
            self._board.append((newgame, goats, carpos))
    
    def getSecondDoor(self, game, choice):
        if game[2] == choice:
            return random.choice(game[1])
        else:
            return game[2]



    def play(self, gamesTotal, doors = 3, switchmode = False):
        self.generateGames(gamesTotal)
        totalsuccess = 0

        for game in self._board:
            playerchoice = random.randint(0, doors-1)
            otherchoice = self.getSecondDoor(game, playerchoice)
            
            choice = playerchoice
    
            if switchmode:
                choice = otherchoice
            
            if game[0][choice] == 1:
                totalsuccess += 1
        
        probs = (totalsuccess/gamesTotal) * 100

        currmode = "Switching" if switchmode else "Staying"

        print(f"{currmode} : {round(probs,3)}%")

gamer = Game()

gamer.play(100000)
            
        

