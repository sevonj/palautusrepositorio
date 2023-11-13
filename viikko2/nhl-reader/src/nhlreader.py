import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url, timeout=30).json()
    print(response[0])

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print_nationality(players, 'FIN')


def print_nationality(players, nationality):

    sorted_players = sorted(
        [player for player in players if player.nationality == nationality],
        reverse=True,
        key=sort_by_points
    )

    print(f"Players from {nationality}:")
    for player in sorted_players:
        print(player)


def sort_by_points(player):
    return player.points
