import requests
from player import Player


def main():
    reader = PlayerReader(
        "https://studies.cs.helsinki.fi/nhlstats/2022-23/players")
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print(f"Players from {"FIN"}:")
    for p in players:
        print(p)

def sort_by_points(player):
    return player.points


class PlayerReader:
    def __init__(self, url):
        response = requests.get(url, timeout=30).json()

        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            [player for player in self.reader.players if player.nationality == nationality],
            reverse=True,
            key=sort_by_points
        )

        # print(f"Players from {nationality}:")
        # for player in sorted_players:
        #    print(player)
