import json

class GameScoreManager:

    def __init__(self):
        self.score = 0
        self.highScore = self.getHighScore()


    def incrementScore(self, amount):
        self.score += amount
        if self.score > self.highScore:
            self.highScore = self.score
            self.updateHighScore()


    def getHighScore(self):
        try:
            with open("./HighScore.json", "r") as file:
                data = json.load(file)
                return data["highscore"]
        except FileNotFoundError:
            print("NOT FOUND")
            return 0


    def updateHighScore(self):
        try:
            with open("./HighScore.json", "w") as file:
                data = {"highscore": int(self.highScore)}
                json.dump(data, file)
        except IOError:
            print("Error: Failed to update high score.")
    
    
    def reset(self):
        self.score = 0