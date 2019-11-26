# File name: map_funcs.py
# -*- coding: utf-8 -*-

"""
This module is used for generating maps for the game and printing them.
"""

import copy


def choose_map_size(*tuple_sizes):
    """
    :param tuple_sizes: tuple or list which have at first index row length and
                        at second index column length.
    :return: a dictionary with sizes given in tuple_sizes. If nothing given,
             returns default sizes 10x10.
    """

    if not tuple_sizes:
        return {'row': 10, 'column': 10}
    else:
        return {'row': tuple_sizes[0], 'column': tuple_sizes[1]}


def create_map(size):
    """
    :param size: a dictionary that is returned by choosePlaneSize() function.
                 It must have sizes in it in this form: {'row': <row size>, 'column': <column size>}.
    :return: returns a matrix list generated with given sizes.
    """

    mp = [['[ ]' for column in range(size['column'])] for row in range(size['row'])]
    return mp


def display_self_and_enemy_map(user_maps):
    """
    :param user_maps: user maps (or matrix list)
    :return: None. This function prints user maps in formatted way.
    """

    u_map = copy.deepcopy(user_maps['self_map'])
    e_map = copy.deepcopy(user_maps['enemy_map'])
    column_size = len(u_map[0])

    print(user_maps['self_name'])
    print('YOUR MAP:' + ' ' * (column_size * 4 - 2) +
          '{0}\'S MAP:'.format(user_maps['enemy_name']))

    for i in range(len(u_map) - 1, -1, -1):

        print('{0} - {1}    {0} - {2}'.format(i,
                                              ' '.join(u_map[i]),
                                              ' '.join(e_map[i])))

    column_list = [' ' + str(n) + ' ' for n in range(column_size)]
    column_string = ' '.join(column_list)
    print('    {0}        {1}'.format(column_string, column_string))


def display_self_map(user_maps):
    # This function helps debugging.
    mp = user_maps['self_map']

    print('{0}\'S MAP:'.format(user_maps['self_name']))

    for i in range(len(mp) - 1, -1, -1):

        print('{0} - {1}'.format(i, ' '.join(mp[i])))

    print('    {0}'.format(' '.join([' ' + str(n) +
                                     ' ' for n in range(len(mp[0]))])))


def display_enemy_map(user_maps):
    # This function helps debugging.
    mp = user_maps['enemy_map']

    print('{0}\'S ENEMY MAP ({1})'.format(user_maps['self_name'],
                                          user_maps['enemy_name']))

    for i in range(len(mp) - 1, -1, -1):

        print('{0} - {1}'.format(i, ' '.join(mp[i])))

    print('    {0}'.format(' '.join([' ' + str(n) +
                                     ' ' for n in range(len(mp[0]))])))
