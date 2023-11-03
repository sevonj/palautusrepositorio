import unittest

from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):

    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        # Haku
        p = self.stats.search("Semenko")
        self.assertNotEqual(p, None)
        self.assertEqual(p.name, "Semenko")
        self.assertEqual(p.team, "EDM")
        self.assertAlmostEqual(p.goals, 4)
        self.assertAlmostEqual(p.assists, 12)
        # Olematon haku
        self.assertEqual(self.stats.search("Taalasmaa"), None)

    def test_team(self):
        # Joukkue
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)
        self.assertEqual(team[0], self.stats._players[0])
        self.assertEqual(team[1], self.stats._players[2])
        self.assertEqual(team[2], self.stats._players[4])
        # Joukkue2
        team = self.stats.team("PIT")
        self.assertEqual(len(team), 1)
        self.assertEqual(team[0], self.stats._players[1])
        # Olematon joukkue
        team = self.stats.team("ÅÄÖ")
        self.assertEqual(len(team), 0)
    
    def test_top(self):
        # Top 1
        top1 = self.stats.top(1)
        self.assertEqual(len(top1), 1)
        self.assertEqual(
            top1,
            [
                self.stats._players[4],
            ]
        )

        # Top 3
        top3 = self.stats.top(3)
        self.assertEqual(len(top3), 3)
        self.assertEqual(
            top3,
            [
                self.stats._players[4],
                self.stats._players[1],
                self.stats._players[3],
            ]
        )