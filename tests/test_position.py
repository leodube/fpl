from fpl.models import Position

position_data = {
    "id": 1,
    "plural_name": "Goalkeepers",
    "plural_name_short": "GKP",
    "singular_name": "Goalkeeper",
    "singular_name_short": "GKP",
    "squad_select": 2,
    "squad_min_select": None,
    "squad_max_select": None,
    "squad_min_play": 1,
    "squad_max_play": 1,
    "ui_shirt_specific": True,
    "sub_positions_locked": [
        12
    ],
    "element_count": 64
}


class TestPosition:
    @staticmethod
    def test_init():
        position = Position(position_data)
        for k, v in position_data.items():
            assert getattr(position, k) == v

    @staticmethod
    def test_str(position):
        assert str(position) == "Goalkeeper"
