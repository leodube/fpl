import pytest

from fpl.utils import (chip_converter, get_current_gameweek, get_headers,
                       logged_in, position_converter, team_converter)


class TestUtils:
    @pytest.mark.asyncio
    async def test_get_current_gameweek(self, fpl):
        current_gameweek = await get_current_gameweek(fpl.session)
        assert isinstance(current_gameweek, int)

    @pytest.mark.asyncio
    async def test_team_converter(self, fpl):
        teams = await fpl.get_teams()
        teams_json = await fpl.get_teams(return_json=True)
        for team in teams:
            assert team_converter(team.id, teams_json) == team.name

    @staticmethod
    def test_position_converter():
        positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
        converted = [position_converter(position) for position in range(1, 5)]
        assert positions == converted

    @staticmethod
    def test_chip_converter():
        chips = ["TC", "WC", "BB", "FH"]
        converted = [chip_converter(chip) for chip in [
            "3xc", "wildcard", "bboost", "freehit"]]

        assert chips == converted

    @pytest.mark.asyncio
    async def test_logged_in(self, fpl):
        await fpl.login()
        assert logged_in(fpl.session)

    @staticmethod
    def test_get_headers():
        headers = get_headers("123")
        assert isinstance(headers, dict)
