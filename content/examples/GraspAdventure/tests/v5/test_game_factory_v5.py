from fixtures_v5 import *  # noqa
from grasp_adventure.data.players import (
    player_list,
    players_in_simple_locations,
    mixed_players,
)


def test_create_object_with_kwargs(a_treasure_chest_description, object_classes):
    factory = GameFactory(a_treasure_chest_description, object_classes)
    tc = factory.create_object("A Treasure Chest")

    assert isinstance(tc, TreasureChest)
    assert tc.gold == 100


def test_create_world():
    factory = GameFactory()
    world = factory.create_world(simple_locations)
    assert world.initial_location_name == "Room 1"
    assert world["Room 1"].name == "Room 1"
    assert world["Room 2"].name == "Room 2"


def test_create_world_twice_raises_error():
    factory = GameFactory()
    factory.create_world(simple_locations)
    with pytest.raises(ValueError):
        factory.create_world(simple_locations)


def test_create_player_from_string():
    factory = GameFactory()
    world = factory.create_world(simple_locations)

    player = factory.create_player("Evil Knievel")

    assert player.name == "Evil Knievel"
    assert player.location == world["Room 1"]


def test_create_player_from_description_without_location():
    factory = GameFactory()
    world = factory.create_world(simple_locations)

    player = factory.create_player({"name": "The Hero"})

    assert player.name == "The Hero"
    assert player.location == world["Room 1"]


def test_create_player_from_description_with_location():
    factory = GameFactory()
    world = factory.create_world(simple_locations)

    player = factory.create_player({"name": "Stealthy Assassin", "location": "Room 2"})

    assert player.name == "Stealthy Assassin"
    assert player.location == world["Room 2"]


def test_create_players_from_strings():
    factory = GameFactory()
    world = factory.create_world(simple_locations)

    players = factory.create_players(player_list)

    assert players[0].name == "Player 1"
    assert players[0].location == world["Room 1"]
    assert players[1].name == "Player 2"
    assert players[1].location == world["Room 1"]


def test_create_players_from_descriptions():
    factory = GameFactory()
    world = factory.create_world(simple_locations)

    players = factory.create_players(players_in_simple_locations)

    assert players[0].name == "Player 1"
    assert players[0].location == world["Room 1"]
    assert players[1].name == "Player 2"
    assert players[1].location == world["Room 2"]
    assert players[2].name == "Player 3"
    assert players[2].location == world["Room 2"]


def test_create_players_from_mixed_data():
    factory = GameFactory()
    world = factory.create_world(simple_locations)

    players = factory.create_players(mixed_players)

    assert players[0].name == "Player 1"
    assert players[0].location == world["Room 1"]
    assert players[1].name == "Player 2"
    assert players[1].location == world["Room 2"]
    assert players[2].name == "Player 3"
    assert players[2].location == world["Room 2"]


def testt_create_world():
    factory = GameFactory()
    game = factory.create_game(simple_locations, mixed_players)

    assert [p.name for p in game.players] == ["Player 1", "Player 2", "Player 3"]
    assert [p.location.name for p in game.players] == ["Room 1", "Room 2", "Room 2"]
    assert game.world.initial_location_name == "Room 1"
