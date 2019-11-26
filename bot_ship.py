# File name: bot_ship.py
# -*- coding: utf-8 -*-

"""
This module is used to create random ships and put them on the map.
"""

import copy
import random
import user_ship


def choose_random_axis():
    """
    :return: returns randomly one of the axis. String with 'horizontal' or 'vertical'
    """

    axis = ['horizontal', 'vertical']
    return random.choice(axis)


def choose_random_horizontal_coordinates(ship_size, bot_map):
    """
    :param ship_size: How much cells the ship takes.
    :param bot_map: Bot map (matrix list) with all the ships.
    :return: returns coordinates in which will be put new ship.
    """

    while True:

        row = random.randint(0, len(bot_map) - 1)
        start_col = random.randint(0, len(bot_map[0]) - 1)
        stop_col = random.randint(0, len(bot_map[0]) - 1)
        start_col, stop_col = min(start_col, stop_col), max(start_col, stop_col)

        if ((stop_col - start_col == ship_size - 1) and
                user_ship.check_horizontal_way(row, start_col, stop_col, bot_map)):

            return {'row': row, 'start_col': start_col, 'stop_col': stop_col}


def put_random_horizontal_ship(ship_size, bot_map):
    """
    :param ship_size: How much cells ship takes.
    :param bot_map: Bot map (matrix list) with all the ships.
    :return: returns updated bot map with new horizontal ship.
    """

    b_m = copy.deepcopy(bot_map)
    crds = choose_random_horizontal_coordinates(ship_size, b_m)

    for col in range(crds['start_col'], crds['stop_col'] + 1):
        b_m[crds['row']][col] = '[S]'

    return b_m


def choose_random_vertical_coordinates(ship_size, bot_map):
    """
    :param ship_size: How much cells ship takes.
    :param bot_map: bot map (matrix list) with all the ships.
    :return: returns random coordinates in which will be put new ship.
    """

    while True:

        col = random.randint(0, len(bot_map[0]) - 1)
        start_row = random.randint(0, len(bot_map) - 1)
        stop_row = random.randint(0, len(bot_map) - 1)
        start_row, stop_row = min(start_row, stop_row), max(start_row, stop_row)

        if ((stop_row - start_row == ship_size - 1) and
                user_ship.check_vertical_way(col, start_row, stop_row, bot_map)):

            return {'col': col, 'start_row': start_row, 'stop_row': stop_row}


def put_random_vertical_ship(ship_size, bot_map):
    """
    :param ship_size: How much cells ship takes.
    :param bot_map: bot map (matrix list) with all the ships.
    :return: returns updated bot map with new vertical ship
    """

    b_m = copy.deepcopy(bot_map)
    crds = choose_random_vertical_coordinates(ship_size, b_m)

    for row in range(crds['start_row'], crds['stop_row'] + 1):
        b_m[row][crds['col']] = '[S]'

    return b_m


def put_random_ship(ship_size, axis, bot_map):
    """
    :param ship_size: How much cells the ship takes.
    :param axis: Chosen axis, string with 'horizontal' or 'vertical'
    :param bot_map: bot map with all the ships.
    :return: returns updated bot map with new ship. Matrix list.
    """

    b_m = copy.deepcopy(bot_map)

    if axis == 'horizontal':
        b_m = put_random_horizontal_ship(ship_size, b_m)

    else:
        b_m = put_random_vertical_ship(ship_size, b_m)

    return b_m


def put_bot_ships_on_map(ships, bot_map):
    """
    :param ships: list of integers with sizes of ships
    :param bot_map: bot map (matrix list) with all the ships
    :return: returns bot map with new ships
    """

    b_m = copy.deepcopy(bot_map)

    for ship in ships:
        b_m['self_map'] = put_random_ship(ship, choose_random_axis(), b_m['self_map'])

    return b_m
