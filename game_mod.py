# File name: game_mod.py
# -*- coding: utf-8 -*-

"""
This module is used to check the game state and for choosing game mode.
Like: bot vs bot, bot vs user, user vs user.
"""


def check_game_map(user_maps, enemy_maps):

    """
    :param user_maps: user maps with all the information about it.
    :param enemy_maps: enemy maps with all the information about it.
    :return:
    """

    all_user_map_string = ''
    all_enemy_map_string = ''

    for i in user_maps['self_map']:

        all_user_map_string += ''.join(i)

    for i in enemy_maps['self_map']:

        all_enemy_map_string += ''.join(i)

    if '[S]' not in all_enemy_map_string:
        print('{0} wins.'.format(enemy_maps['enemy_name']))
        quit()

    if '[S]' not in all_user_map_string:
        print('{0} wins.'.format(user_maps['enemy_name']))
        quit()
