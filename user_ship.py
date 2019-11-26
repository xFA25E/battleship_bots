# File name: user_ship.py
# -*- coding: utf-8 -*-

"""
This module is used for creating user ships and put them on the user plane.
"""

import copy
import map_funcs


def choose_axis():
    """
    :return: returns string with on of the axis. Horizontal or vertical.
    """

    a_s = ['horizontal', 'vertical']

    while True:
        axis = input('Choose axis: 0 - horizontal, 1 - vertical.')
        axis = int(axis) if axis.isnumeric() else -1

        if axis == 0:
            return a_s[0]
        elif axis == 1:
            return a_s[1]

        print('Error, retry')


def check_horizontal_way(row, start_col, stop_col, user_map):
    """
    :param row: is the chosen row on the map.
    :param start_col: the chosen starting point of columns for new ship.
    :param stop_col: the chosen ending point of coulmns for new ship.
    :param user_map: user map with all the ships.
    :return: returns True if no ships are in the chosen coordinates. If vice versa
             returns False.
    """

    # print('I AM DEBUGGING HELPER ON FUNCTION check_horizontal_way().' +
    #       'row, st_row, sp_row = {0}'.format((row, start_col, stop_col)))

    if row == 0:
        rows = [row, row + 1]

    elif row == (len(user_map) - 1):
        rows = [row, row - 1]

    else:
        rows = [row, row + 1, row - 1]

    if start_col == 0:
        st_col, sp_col = start_col, stop_col + 2

    elif stop_col == (len(user_map[0]) - 1):
        st_col, sp_col = start_col - 1, stop_col + 1

    else:
        st_col, sp_col = start_col - 1, stop_col + 2

    for col in range(st_col, sp_col):
        for rw in rows:
            if user_map[rw][col] == '[S]':
                return False
    return True


def choose_horizontal_coordinates(ship_size, user_map):
    """
    :param ship_size: How much cells ship takes.
    :param user_map: user map with all the ships.
    :return: returns chosen coordinates for the ship. If they are in error,
             returns None, None, None
    """

    row = input('Choose row: ')
    row = int(row) if row.isnumeric() else -1

    if (row >= 0) and (row < len(user_map)):

        start_col = input('From column: ')
        stop_col = input('To column: ')

        start_col = int(start_col) if start_col.isnumeric() else -1
        stop_col = int(stop_col) if stop_col.isnumeric() else -1

        start_col, stop_col = min(start_col, stop_col), max(start_col, stop_col)

        # print('I AM DEBUGGING HELPER ON FUNCTION put_horizontal_coordinates().' +
        #       'row, st_row, sp_row = {0}'.format((row, start_col, stop_col)))

        if ((start_col >= 0) and (start_col < len(user_map[0])) and
                (stop_col >= 0) and (stop_col < len(user_map[0])) and
                (stop_col - start_col == ship_size - 1) and
                check_horizontal_way(row, start_col, stop_col, user_map)):

            return {'row': row, 'start_col': start_col, 'stop_col': stop_col}

    print('The coordinates are too large or too small or they are not numeric.')


def put_horizontal_ship(ship_size, user_map):
    """
    :param ship_size: How much cells ship takes.
    :param user_map: User map with all the ships.
    :return: returns updated user map with all the ships +
             new ship.
    """

    u_m = copy.deepcopy(user_map)

    crds = choose_horizontal_coordinates(ship_size, u_m)

    # print('I AM DEBUGGING HELPER ON FUNCTION put_horizontal_ship().' +
    #       '{0}'.format(crds))

    if crds:

        for col in range(crds['start_col'], crds['stop_col'] + 1):

            u_m[crds['row']][col] = '[S]'

        return u_m

    else:
        return put_ship(ship_size, choose_axis(), user_map)


def check_vertical_way(col, start_row, stop_row, user_map):
    """
    :param col: Chosen column or the user map.
    :param start_row: chosen starting point of row for new ship.
    :param stop_row: chosen ending point of row for new ship.
    :param user_map: user map with all the ships.
    :return: returns True if no ships are in the chosen coordinates. If vice versa
             returns False.
    """

    # print('I AM DEBUGGING HELPER ON FUNCTION check_vertical_way().' +
    #       'col, st_row, sp_row = {0}'.format((col, start_row, stop_row)))

    if col == 0:
        cols = [col, col + 1]

    elif col == (len(user_map[0]) - 1):
        cols = [col, col - 1]

    else:
        cols = [col, col - 1, col + 1]

    if start_row == 0:
        st_row, sp_row = start_row, stop_row + 2

    elif stop_row == (len(user_map) - 1):
        st_row, sp_row = start_row - 1, stop_row + 1

    else:
        st_row, sp_row = start_row - 1, stop_row + 2

    for row in range(st_row, sp_row):
        for cl in cols:
            if user_map[row][cl] == '[S]':
                return False
    return True


def choose_vertical_coordinates(ship_size, user_map):
    """
    :param ship_size: How much cells the ship takes.
    :param user_map: User map with all the ships.
    :return: returns the chosen coordinates for new ship. If they are in error,
             returns None, None, None
    """

    col = input('Choose column: ')
    col = int(col) if col.isnumeric() else -1

    if (col >= 0) and (col < len(user_map[0])):

        start_row = input('From row: ')
        stop_row = input('To row: ')

        start_row = int(start_row) if start_row.isnumeric() else -1
        stop_row = int(stop_row) if stop_row.isnumeric() else -1

        start_row, stop_row = min(start_row, stop_row), max(start_row, stop_row)
        # print('I AM DEBUGGING HELPER ON FUNCTION choose_vertical_coordinates()' +
        #       'col, st_row, sp_row = {0}'.format((col, start_row, stop_row)))

        if ((start_row >= 0) and (start_row < len(user_map)) and
                (stop_row >= 0) and (stop_row < len(user_map)) and
                (stop_row - start_row == ship_size - 1) and
                check_vertical_way(col, start_row, stop_row, user_map)):

            return {'col': col, 'start_row': start_row, 'stop_row': stop_row}

    print('The coordinates are too large or too small or they are not numeric.')


def put_vertical_ship(ship_size, user_map):
    """
    :param ship_size: How much cells the ship takes.
    :param user_map: User map with all the ships.
    :return: returns updated user map with all the ships +
             new ship.
    """

    u_m = copy.deepcopy(user_map)

    crds = choose_vertical_coordinates(ship_size, u_m)
    # print('I AM DEBUGGING HELPER ON FUNCTION put_vertical_ship().' +
    #       '{0}'.format(crds))

    if crds:

        for row in range(crds['start_row'], crds['stop_row'] + 1):

            u_m[row][crds['col']] = '[S]'

        return u_m

    else:
        return put_ship(ship_size, choose_axis(), user_map)


def put_ship(ship_size, axis, user_map):
    """
    :param ship_size: How much cells the ship takes.
    :param axis: The chosen axis for the ship.
    :param user_map: user map with all the ships.
    :return: returns user map with all the ships +
             the new once.
    """

    u_m = copy.deepcopy(user_map)

    print('Ship size is {0}.'.format(ship_size))
    print('The axis is {0}'.format(axis))

    if axis == 'horizontal':
        u_m = put_horizontal_ship(ship_size, u_m)

    else:
        u_m = put_vertical_ship(ship_size, u_m)

    return u_m


def put_user_ships_on_map(ships, user_maps):
    """
    :param ships: the list of ships (their sizes) that will be put on the map
    :param user_maps: user maps (self and enemy)
    :return: returns user maps with new ships.
    """

    u_m = copy.deepcopy(user_maps)

    for ship in ships:
        map_funcs.display_self_and_enemy_map(u_m)
        u_m['self_map'] = put_ship(ship, choose_axis(), u_m['self_map'])

    return u_m
