from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or, QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(HasAtLeast(5, "goals"), HasAtLeast(20, "assists"), PlaysIn("PHI"))

    matcher = And(
        HasAtLeast(70, "points"), Or(PlaysIn("NYR"), PlaysIn("FLA"), PlaysIn("BOS"))
    )

    query = QueryBuilder()
    matcher = (
        query.plays_in("NYR")
        .has_at_least(1, "goals")
        .has_fewer_than(10, "assists")
        .query()
    )
    m1 = query.plays_in("PHI").has_at_least(10, "assists").has_fewer_than(5, "goals").query()

    m2 = query.plays_in("EDM").has_at_least(50, "points").query()

    matcher = query.incl_or(m1, m2).query()

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
