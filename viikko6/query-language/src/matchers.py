class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class All:
    def __init__(self):
        pass

    def test(self, player):
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value >= self._value


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return not player_value >= self._value


class Query:
    def __init__(self) -> None:
        self._matchers = [All()]


class QueryBuilder:
    def __init__(self, matcher=All()) -> None:
        self._matcher = matcher

    def query(self):
        return self._matcher

    def plays_in(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def has_at_least(self, val, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(val, attr)))

    def has_fewer_than(self, val, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(val, attr)))

    def incl_or(self, *matchers):
        return QueryBuilder(Or(*matchers))
