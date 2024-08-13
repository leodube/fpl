Gameweek
================

Information for the :class:`Position <fpl.models.position.Position>` is taken from e.g. the following endpoints:
  https://fantasy.premierleague.com/api/bootstrap-static/


An example of part of what information a :class:`Position <fpl.models.position.Position>` contains is shown below:

.. code-block:: javascript

  {
    "id": 1,
    "plural_name": "Goalkeepers",
    "plural_name_short": "GKP",
    "singular_name": "Goalkeeper",
    "singular_name_short": "GKP",
    "squad_select": 2,
    "squad_min_select": null,
    "squad_max_select": null,
    "squad_min_play": 1,
    "squad_max_play": 1,
    "ui_shirt_specific": true,
    "sub_positions_locked": [
      12
    ],
    "element_count": 64
    }

Basic usage:

.. code-block:: python

  from fpl import FPL
  import aiohttp
  import asyncio
  
  async def main():
      async with aiohttp.ClientSession() as session:
          fpl = FPL(session)
          position = await fpl.get_position(1)
      print(position)

  # Python 3.7+
  asyncio.run(main())
  ...
  # Python 3.6
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  # Goalkeeper

.. autoclass:: fpl.models.position.Position
   :members:
