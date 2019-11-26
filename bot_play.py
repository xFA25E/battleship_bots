# File name: bot_play.py
# -*- coding: utf-8 -*-

"""
This module is used to make bot turns.
"""

import copy

import map_funcs

import game_mod

import random

import user_play

import time


def choose_random_shoot_coordinates(map_to_hit):
    """
    :param map_to_hit: map with ships (matrix list).
    :return: returns dictionary with coordinates.
    """

    while True:

        row = random.randint(0, len(map_to_hit) - 1)
        column = random.randint(0, len(map_to_hit[0]) - 1)

        if map_to_hit[row][column] != '[X]' and map_to_hit[row][column] != '[W]':
            return {'row': row, 'column': column}


def initialize_point_try(hit_point, enemy_map):
    """
    :param hit_point: coordinates where the ship was hit.
    :param enemy_map: enemy map with all the ships.
    :return: returns the list with dictionaries with coordinates to try.
    """

    point_try = []

    if hit_point['row'] == 0:
        point_try.append({'column': hit_point['column'], 'row': hit_point['row'] + 1})

    elif hit_point['row'] == len(enemy_map) - 1:
        point_try.append({'column': hit_point['column'], 'row': hit_point['row'] - 1})

    else:
        point_try.append({'column': hit_point['column'], 'row': hit_point['row'] - 1})
        point_try.append({'column': hit_point['column'], 'row': hit_point['row'] + 1})

    if hit_point['column'] == 0:
        point_try.append({'row': hit_point['row'], 'column': hit_point['column'] + 1})

    elif hit_point['column'] == len(enemy_map[0]) - 1:
        point_try.append({'row': hit_point['row'], 'column': hit_point['column'] - 1})

    else:
        point_try.append({'row': hit_point['row'], 'column': hit_point['column'] + 1})
        point_try.append({'row': hit_point['row'], 'column': hit_point['column'] - 1})

    print('Init point_try. {0}'.format(point_try))

    def check_x(point):

        if enemy_map[point['row']][point['column']] == '[X]':
            return False
        else:
            return True

    point_try = list(filter(check_x, point_try))

    print('point_try', point_try)

    return point_try


def choose_random_point_try_coordinates(user_maps):
    """
    :param user_maps: user maps with all the information about it.
    :return: returns user maps with updated next_hit_point.
    """

    u_m = copy.deepcopy(user_maps)

    random_point_try = random.choice(u_m['bot_memory']['point_try'])
    ind = u_m['bot_memory']['point_try'].index(random_point_try)

    u_m['bot_memory']['next_hit_point'] = u_m['bot_memory']['point_try'].pop(ind)

    return u_m


def check_current_ship_state(user_maps, enemy_maps):
    """
    :param user_maps: user maps with all the information about it.
    :param enemy_maps: enemy maps with all the information about it.
    :return: returns False if ship was destroyed or True if ship was not destroyed.
    """

    all_point_string = ''

    if not user_maps['bot_memory']['axis']:

        row = user_maps['bot_memory']['point_hit'][0]['row']
        column = user_maps['bot_memory']['point_hit'][0]['column']

        if row == 0:
            all_point_string += enemy_maps['self_map'][row + 1][column]

        elif row == len(enemy_maps['self_map']) - 1:
            all_point_string += enemy_maps['self_map'][row - 1][column]

        else:
            all_point_string += enemy_maps['self_map'][row - 1][column]
            all_point_string += enemy_maps['self_map'][row + 1][column]

        if column == 0:
            all_point_string += enemy_maps['self_map'][row][column + 1]

        elif column == len(enemy_maps['self_map'][0]) - 1:
            all_point_string += enemy_maps['self_map'][row][column - 1]

        else:
            all_point_string += enemy_maps['self_map'][row][column + 1]
            all_point_string += enemy_maps['self_map'][row][column - 1]

    elif user_maps['bot_memory']['axis'] == 'vertical':

        column = user_maps['bot_memory']['point_hit'][0]['column']
        rows = [r['row'] for r in user_maps['bot_memory']['point_hit']]

        row_min, row_max = min(rows), max(rows)

        if row_min == 0:
            all_point_string += enemy_maps['self_map'][row_max + 1][column]

        elif row_max == len(enemy_maps['self_map']) - 1:
            all_point_string += enemy_maps['self_map'][row_min - 1][column]

        else:
            all_point_string += enemy_maps['self_map'][row_min - 1][column]
            all_point_string += enemy_maps['self_map'][row_max + 1][column]

    else:

        row = user_maps['bot_memory']['point_hit'][0]['row']
        cols = [r['column'] for r in user_maps['bot_memory']['point_hit']]

        col_min, col_max = min(cols), max(cols)

        if col_min == 0:
            all_point_string += enemy_maps['self_map'][row][col_max + 1]

        elif col_max == len(enemy_maps['self_map'][0]) - 1:
            all_point_string += enemy_maps['self_map'][row][col_min - 1]

        else:
            all_point_string += enemy_maps['self_map'][row][col_min - 1]
            all_point_string += enemy_maps['self_map'][row][col_max + 1]

    print('all_point_string', all_point_string)

    if '[S]' in all_point_string:
        state = True
    else:
        state = False

    return state


def choose_vertical_point_try(point_hit, enemy_map):
    """
    :param point_hit: the list with points in which enemy ship was hit.
    :param enemy_map: enemy map with all the ships.
    :return: returns list of vertical points to try to shoot.
    """

    point_try = []
    print('point_try', point_try)

    print('point_hit', point_hit)
    rows = [r['row'] for r in point_hit]
    column = point_hit[0]['column']
    print('rows, column: ', rows, column)

    row_min, row_max = min(rows), max(rows)
    print('row_min, row_max: ', row_min, row_max)

    if row_min == 0:
        point_try.append({'column': column, 'row': row_max + 1})

    elif row_max == len(enemy_map) - 1:
        point_try.append({'column': column, 'row': row_min - 1})

    else:
        point_try.append({'column': column, 'row': row_max + 1})
        point_try.append({'column': column, 'row': row_min - 1})

    print('point_try', point_try)

    if enemy_map[point_try[0]['row']][point_try[0]['column']] == '[X]':
        point_try.pop(0)
    elif len(point_try) == 2:
        if enemy_map[point_try[1]['row']][point_try[1]['column']] == '[X]':
            point_try.pop(1)

    print('point_try', point_try)

    return point_try


def choose_horizontal_point_try(point_hit, enemy_map):
    """
    :param point_hit: list with points in which enemy ship was hit.
    :param enemy_map: enemy map with all the ships.
    :return: returns list with horizontal points to try to shoot.
    """

    point_try = []
    print('Point_try', point_try)

    print('point_hit', point_hit)
    cols = [r['column'] for r in point_hit]
    row = point_hit[0]['row']
    print('cols and row: ', cols, row)

    col_min, col_max = min(cols), max(cols)
    print('col_min, col_max: ', col_min, col_max)

    if col_min == 0:
        point_try.append({'column': col_max + 1, 'row': row})

    elif col_max == len(enemy_map[0]) - 1:
        point_try.append({'column': col_min - 1, 'row': row})

    else:
        point_try.append({'column': col_max + 1, 'row': row})
        point_try.append({'column': col_min - 1, 'row': row})

    print('point_try', point_try)

    if enemy_map[point_try[0]['row']][point_try[0]['column']] == '[X]':
        point_try.pop(0)
    elif len(point_try) == 2:
        if enemy_map[point_try[1]['row']][point_try[1]['column']] == '[X]':
            point_try.pop(1)

    print('point_try', point_try)

    return point_try


def update_bot_memory(user_maps, enemy_maps):
    """
    :param user_maps: user maps with all the information about them.
    :param enemy_maps: enemy maps with all the information about them.
    :return: return updated bot memory with new points to try to shoot.
    """

    b_mem = copy.deepcopy(user_maps['bot_memory'])

    if b_mem['target_hit']:

        print('There is target_hit')

        if not b_mem['axis']:

            print('But no chosen axis.')

            if b_mem['next_hit_point']['row'] == b_mem['point_hit'][0]['row']:
                b_mem['axis'] = 'horizontal'

            else:
                b_mem['axis'] = 'vertical'

            print('Chosen axis is: {0}'.format(b_mem['axis']))

        b_mem['point_hit'].append(copy.deepcopy(b_mem['next_hit_point']))

        if b_mem['axis'] == 'vertical':
            b_mem['point_try'] = choose_vertical_point_try(b_mem['point_hit'],
                                                           enemy_maps['self_map'])

        else:
            b_mem['point_try'] = choose_horizontal_point_try(b_mem['point_hit'],
                                                             enemy_maps['self_map'])

        print('Points to try are: {0}'.format(b_mem['point_try']))

    return b_mem


def fill_bot_memory_after_destroyed_ship(bot_memory, enemy_map):
    """
    :param bot_memory: dictionary with data that needs to bot.
    :param enemy_map: enemy map with all ships.
    :return: returns updated bot memory with random next_hit_point.
    """

    b_mem = copy.deepcopy(bot_memory)

    b_mem['point_hit'] = []
    b_mem['point_try'] = []
    b_mem['axis'] = ''
    b_mem['target_hit'] = False
    b_mem['next_hit_point'] = choose_random_shoot_coordinates(enemy_map)

    return b_mem


def put_halo_around(point, enemy_map):
    """
    :param point: point in which shot was successful.
    :param enemy_map: enemy map with all the ships.
    :return: return updated enemy map with Xs around destroyed ship.
    """

    e_m = copy.deepcopy(enemy_map)

    if point['row'] == 0:
        rows = [point['row'], point['row'] + 1]

    elif point['row'] == len(enemy_map) - 1:
        rows = [point['row'], point['row'] - 1]

    else:
        rows = [point['row'], point['row'] - 1, point['row'] + 1]

    if point['column'] == 0:
        cols = [point['column'], point['column'] + 1]

    elif point['column'] == len(enemy_map[0]) - 1:
        cols = [point['column'], point['column'] - 1]

    else:
        cols = [point['column'], point['column'] - 1, point['column'] + 1]

    for row in rows:
        for col in cols:
            e_m[row][col] = '[X]'
    e_m[rows[0]][cols[0]] = '[W]'

    return e_m


def put_vertical_halo_around(point_hit, enemy_map):
    """
    :param point_hit: list with successful shot points.
    :param enemy_map: enemy map with all the ships.
    :return: returns updated enemy map with Xs around destroyed ship.
    """

    e_m = copy.deepcopy(enemy_map)

    rows = [r['row'] for r in point_hit]
    min_row, max_row = min(rows), max(rows)
    column = point_hit[0]['column']

    if min_row == 0:
        st_row, sp_row = min_row, max_row + 1

    elif max_row == len(e_m) - 1:
        st_row, sp_row = min_row - 1, max_row

    else:
        st_row, sp_row = min_row - 1, max_row + 1

    if column == 0:
        cols = [column, column + 1]

    elif column == len(e_m[0]) - 1:
        cols = [column, column - 1]

    else:
        cols = [column, column - 1, column + 1]

    for row in range(st_row, sp_row + 1):
        for col in cols:
            e_m[row][col] = '[X]'

    for row in range(min_row, max_row + 1):
        e_m[row][column] = '[W]'

    return e_m


def put_horizontal_halo_around(point_hit, enemy_map):
    """
    :param point_hit: list with successful shot points.
    :param enemy_map: enemy map with all ships.
    :return: returns updated enemy map with Xs around destroyed ship.
    """

    e_m = copy.deepcopy(enemy_map)

    cols = [c['column'] for c in point_hit]
    min_col, max_col = min(cols), max(cols)
    row = point_hit[0]['row']

    if min_col == 0:
        st_col, sp_col = min_col, max_col + 1

    elif max_col == len(e_m) - 1:
        st_col, sp_col = min_col - 1, max_col

    else:
        st_col, sp_col = min_col - 1, max_col + 1

    if row == 0:
        rows = [row, row + 1]

    elif row == len(e_m[0]) - 1:
        rows = [row, row - 1]

    else:
        rows = [row, row - 1, row + 1]

    for col in range(st_col, sp_col + 1):
        for roww in rows:
            e_m[roww][col] = '[X]'

    for col in range(min_col, max_col + 1):
        e_m[row][col] = '[W]'

    return e_m


def put_xs_around_destroyed_ship(bot_memory, enemy_map):
    """
    :param bot_memory: bot memory with all necessary information.
    :param enemy_map: enemy map with all ships.
    :return: returns updated enemy map with Xs around destroyed ship.
    """

    e_m = copy.deepcopy(enemy_map)
    point_hit = bot_memory['point_hit']
    axis = bot_memory['axis']

    if not axis and len(point_hit) == 1:
        e_m = put_halo_around(point_hit[0], e_m)

    elif axis == 'vertical':
        e_m = put_vertical_halo_around(point_hit, e_m)

    else:
        e_m = put_horizontal_halo_around(point_hit, e_m)

    return e_m


def choose_bot_shoot_coordinates(user_maps, enemy_maps):
    """
    :param user_maps: user maps with all necessary information.
    :param enemy_maps: enemy maps with all necessary information.
    :return: return user maps with updated next_hit_point in bot memory.
    """

    u_m, e_m = copy.deepcopy(user_maps), copy.deepcopy(enemy_maps)

    if not u_m['bot_memory']['point_hit']:

        print('There is no point_hit.')

        print('There is no target_hit. I have to choose random coordinates.')

        u_m['bot_memory']['next_hit_point'] = choose_random_shoot_coordinates(e_m['self_map'])

    elif (check_current_ship_state(u_m, e_m) and not u_m['bot_memory']['point_try'] and
          len(u_m['bot_memory']['point_hit']) == 1):

        print('The ship is still in live. I have to initialize point_try')

        u_m['bot_memory']['point_try'] = initialize_point_try(u_m['bot_memory']['point_hit'][0],
                                                              e_m['self_map'])

        print('And choose random point_try.')

        u_m = choose_random_point_try_coordinates(u_m)

    elif len(u_m['bot_memory']['point_hit']) == 2:

        print('There is 2 successful hits. So I need to choose axis.')

        u_m['bot_memory'] = update_bot_memory(u_m, e_m)

        if check_current_ship_state(u_m, e_m):

            print('Ship is not destroyed. Choosing random point_try')

            u_m = choose_random_point_try_coordinates(u_m)

        else:

            print('Ship is destroyed. Need to update my memory with new data.')
            print('point_hit'.format(u_m['bot_memory']['point_hit']))

            e_m['self_map'] = put_xs_around_destroyed_ship(u_m['bot_memory'], e_m['self_map'])
            u_m['bot_memory'] = fill_bot_memory_after_destroyed_ship(u_m['bot_memory'],
                                                                     e_m['self_map'])

    elif check_current_ship_state(u_m, e_m):

        print('There is point_hit. So i need to update and init next point_try.')
        print('Choosing random point_try ...')

        u_m['bot_memory'] = update_bot_memory(u_m, e_m)
        u_m = choose_random_point_try_coordinates(u_m)

    else:

        print('The current ship was destroyed. Need to update my memory with new data.')
        print('point_hit'.format(u_m['bot_memory']['point_hit']))

        e_m['self_map'] = put_xs_around_destroyed_ship(u_m['bot_memory'], e_m['self_map'])
        u_m['bot_memory'] = fill_bot_memory_after_destroyed_ship(u_m['bot_memory'],
                                                                 e_m['self_map'])

    print('Chosen point is: {0}'.format(u_m['bot_memory']['next_hit_point']))

    return u_m, e_m


def play_bot_turn(user_maps, enemy_maps):
    """
    :param user_maps: user maps with necessary information.
    :param enemy_maps: enemy maps with necessary information.
    :return: returns updated user and enemy maps with new shots on maps and destroyed ships.
    """

    u_m = copy.deepcopy(user_maps)
    e_m = copy.deepcopy(enemy_maps)

    while True:

        input()
        # time.sleep(0.5)
        print('{0} turn.'.format(user_maps['self_name']))
        print('Bot memory: {0}'.format(u_m['bot_memory']))

        map_funcs.display_self_and_enemy_map(u_m)
        map_funcs.display_self_map(e_m)

        u_m, e_m = choose_bot_shoot_coordinates(u_m, e_m)
        u_m, e_m, u_m['bot_memory']['target_hit'] = user_play.update_map_after_shoot(u_m['bot_memory']['next_hit_point'],
                                                                                     u_m,
                                                                                     e_m)

        game_mod.check_game_map(u_m, e_m)

        print('Bot memory: {0}'.format(u_m['bot_memory']))
        print('=' * 60)

        if not u_m['bot_memory']['target_hit']:
            map_funcs.display_self_and_enemy_map(u_m)
            map_funcs.display_self_map(e_m)
            return u_m, e_m

        else:
            u_m['bot_memory']['point_hit'].append(u_m['bot_memory']['next_hit_point'])
