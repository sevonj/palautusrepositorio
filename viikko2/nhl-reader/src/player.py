class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.team = dict['team']
        self.games = dict['games']
   
    def __str__(self):
        return " ".join([
            f"{self.name:22}",
            f"{self.team:4}",
            f"{self.goals:2} +",
            f"{self.assists:2} =",
            f"{self.points:3}",
        ])
    
    @property
    def points(self):
        return self.goals + self.assists
    