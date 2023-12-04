class TennisGame:
    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, p_name):
        match p_name:
            case self.p1_name:
                self.p1_score += 1
            case self.p2_name:
                self.p2_score += 1
            case _:
                raise ValueError(f"{p_name} not a player!")

    def get_score(self):

        # Even
        if self.p1_score == self.p2_score:
            if self.p1_score >= 3:
                return "Deuce"
            else:
                return f"{get_scorename(self.p1_score)}-All"

        # Advantage
        elif max(self.p1_score, self.p2_score) >= 4:
            score_diff = abs(self.p1_score - self.p2_score)
            top_player: str
            if self.p1_score > self.p2_score:
                top_player = "player1"
            else:
                top_player = "player2"

            match score_diff:
                case 1:
                    return f"Advantage {top_player}"
                case _: # Score difference is larger than 1
                    return f"Win for {top_player}"

        # Normal
        else:
            p1_str = get_scorename(self.p1_score)
            p2_str = get_scorename(self.p2_score)
            return f"{p1_str}-{p2_str}"



def get_scorename(score: int) -> str:
    match score:
        case 0:
            return "Love"
        case 1:
            return "Fifteen"
        case 2:
            return "Thirty"
        case 3:
            return "Forty"
        case _:
            raise ValueError("Score is outside expected range!")
