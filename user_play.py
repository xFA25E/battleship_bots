# File name: user_play.py
# -*- coding: utf-8 -*-

"""
This module is used for playing battleship, to make actual turns by player.
"""

import copy
import map_funcs
import game_mod


def choose_shoot_coordinates(enemy_map):
    """
    :param enemy_map: matrix list, it is used to discover map sizes.
    :return: return a dictionary with chosen coordinates. {'row': row, 'column': column}
    """

    while True:

        row = input('Shoot row: ')
        row = int(row) if row.isnumeric() else -1

        column = input('Shoot column: ')
        column = int(column) if column.isnumeric() else -1

        if ((row >= 0) and (row < len(enemy_map)) and
                (column >= 0) and (column < len(enemy_map[0]))):

            return {'row': row, 'column': column}

        print('The chosen coordinates are too large or too small or they are not numeric.')


def update_map_after_shoot(coordinates, user_maps, enemy_map):
    """
    :param coordinates: dictionary with chosen coordinates, {'row': row, 'column': column}
    :param user_maps: user maps and all the information about it.
    :param enemy_map: enemy map and all the information about it.
    :return: returns user maps and enemy map. Updated.
    """

    u_m = copy.deepcopy(user_maps)
    e_m = copy.deepcopy(enemy_map)

    sign = e_m['self_map'][coordinates['row']][coordinates['column']]

    if sign == '[S]':
        u_m['enemy_map'][coordinates['row']][coordinates['column']] = '[W]'
        e_m['self_map'][coordinates['row']][coordinates['column']] = '[W]'
        hit = True
        print('{0} hit.'.format(u_m['self_name']))

    else:
        u_m['enemy_map'][coordinates['row']][coordinates['column']] = '[X]'
        e_m['self_map'][coordinates['row']][coordinates['column']] = '[X]'
        hit = False
        print('{0} miss.'.format(u_m['self_name']))

    return u_m, e_m, hit


def play_user_turn(user_maps, enemy_maps):
    """
    :param user_maps: user maps and all the information about it.
    :param enemy_maps: enemy maps and all the information about it.
    :return: returns updated maps with new ships or not.
    """

    u_m = copy.deepcopy(user_maps)
    e_m = copy.deepcopy(enemy_maps)

    while True:

        print('{0}\' turn.'.format(u_m['self_name']))

        map_funcs.display_self_and_enemy_map(u_m)
        map_funcs.display_self_map(e_m)
        coordinates = choose_shoot_coordinates(e_m['self_map'])
        u_m, e_m, target_hit = update_map_after_shoot(coordinates, u_m, e_m)

        game_mod.check_game_map(u_m, e_m)

        if not target_hit:
            return u_m, e_m
