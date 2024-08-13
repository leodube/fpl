class Position():
    """A class representing a player's position in Fantasy Premier League."""

    def __init__(self, position_information):
        for k, v in position_information.items():
            setattr(self, k, v)

    def __str__(self):
        return f"{self.singular_name}"
