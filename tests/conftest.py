import aiohttp
import pytest
import pytest_asyncio
import os

from fpl import FPL
from fpl.models import Fixture, H2HLeague, User, ClassicLeague, Team, Gameweek, Position
from tests.test_classic_league import classic_league_data
from tests.test_fixture import fixture_data
from tests.test_h2h_league import h2h_league_data
from tests.test_team import team_data
from tests.test_user import user_data
from tests.test_gameweek import gameweek_data
from tests.test_position import position_data

try:
    from.temp_env_var import TEMP_ENV_VARS, ENV_VARS_TO_SUSPEND
except ImportError:
    TEMP_ENV_VARS = {}
    ENV_VARS_TO_SUSPEND = []

@pytest.fixture(scope="session", autouse=True)
def tests_setup_and_teardown():
    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_ENV_VARS)
    for env_var in ENV_VARS_TO_SUSPEND:
        os.environ.pop(env_var, default=None)

    yield
    # Will be executed after the last test
    os.environ.clear()
    os.environ.update(old_environ)

@pytest_asyncio.fixture()
async def fpl():
    session = aiohttp.ClientSession()
    fpl = FPL(session)
    yield fpl
    await session.close()


@pytest_asyncio.fixture()
async def classic_league():
    session = aiohttp.ClientSession()
    yield ClassicLeague(classic_league_data, session)
    await session.close()


@pytest_asyncio.fixture()
async def gameweek():
    return Gameweek(gameweek_data)


@pytest_asyncio.fixture()
async def player(fpl):
    yield await fpl.get_player(345, include_summary=True)


@pytest_asyncio.fixture()
async def position():
    return Position(position_data)


@pytest.fixture()
async def settings(fpl):
    yield await fpl.game_settings()


@pytest_asyncio.fixture()
async def team():
    session = aiohttp.ClientSession()
    yield Team(team_data, session)
    await session.close()


@pytest.fixture()
def fixture():
    return Fixture(fixture_data)


@pytest_asyncio.fixture()
async def h2h_league():
    session = aiohttp.ClientSession()
    yield H2HLeague(h2h_league_data, session)
    await session.close()


@pytest_asyncio.fixture()
async def user():
    session = aiohttp.ClientSession()
    yield User(user_data, session)
    await session.close()
