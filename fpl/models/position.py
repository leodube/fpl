class Postion():
    """A class representing a player's position in Fantasy Premier League."""

    def __init__(self, player_information):
        for k, v in player_information.items():
            setattr(self, k, v)

    def __str__(self):
        return f"{self.singular_name}"
