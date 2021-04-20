from getpass import getpass # use this to hide the play from other players

class RPSPlayer():
    # A player used in RockPaperScisors
    def __init__(self, name: str):
        self.name = name
        self.position = ""

    def shoot(self, play: str):
      # set the value of self.position
      self.position = play

class RockPaperScisors():
    # Class to play a game of Rock/Paper/Scisors
    def __init__(self, players_by_name):
        self.players = [RPSPlayer(name) for name in players_by_name]

    def play(self): # players make a move

        player_choice = ""
        for player in self.players: #all players make a move
            while player_choice not in ("R","P","S"): # moves can only be R, P, or S
                player_choice = getpass(f"{player.name} make your move:(R,P,S):").upper()
            player.shoot(player_choice)
            player_choice = "" #reset the variable used in the while loop

        self._check_win()

    def _check_win(self):
        # evaluate all the positions to see if a player won and print the winner or tie.
        for index, player in enumerate(self.players):
            other_plays = [other_player.position for other_index, other_player in enumerate(self.players) if other_index != index]
            if player.position == "R" and "R" not in other_plays and "P" not in other_plays:
                print(f"{player.name} won")
                return True
            elif player.position == "P" and "S" not in other_plays and "P" not in other_plays:
                print(f"{player.name} won")
                return True
            elif player.position == "S" and "R" not in other_plays and "S" not in other_plays:
                print(f"{player.name} won")
                return True
        print("It is a tie, try again")
        return False

if __name__ == "__main__":
    RPS_game = RockPaperScisors(["Bob", "Alice", "Charlie"])
    RPS_game.play()
