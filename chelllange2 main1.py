class player:
    def play(self):
        print("the plkayer is playing cricket.")

class Batsman(player):
    def play(self):
        print("the batsman is batting.")

class Bowler(player):
    def play(self):
        print("The bowler is bowling.")

batsman = Batsman()
bowler = Bowler()


batsman.play()
bowler.play(