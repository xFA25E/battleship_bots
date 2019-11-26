# -*- coding: utf-8 -*-

import map_funcs
import user_ship
import bot_ship
import user_play
import bot_play
import copy

bot_one_name = 'Bot One'
bot_two_name = 'Bot Two'

ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

# bot_memory = {'enemy_ships': [4, 3, 3, 2, 2, 2, 1, 1, 1, 1],
#               'start_hit_point': {'row': int, 'column': int},
#               'direction_try': ['not_sure' or 'sure', ('left' or 'right') or ('up' or 'down')],
#               'axis_try': ['not_sure' or 'sure', 'horizontal' or 'vertical'],
#               'boat_hits': int, # if max(*bot_memory['ships_all'])) break
#               'fault_hits': int } # if max(*bot_memory['ships_all']))}

bot_memory = {'point_hit': [],
              'point_try': [],
              'axis': '',
              'target_hit': False,
              'next_hit_point': {}}

bot_one_maps = {'self_map': map_funcs.create_map(map_funcs.choose_map_size()),
                'enemy_map': map_funcs.create_map(map_funcs.choose_map_size()),
                'self_name': bot_one_name,
                'enemy_name': bot_two_name,
                'bot_memory': copy.deepcopy(bot_memory)}

bot_two_maps = {'self_map': map_funcs.create_map(map_funcs.choose_map_size()),
                'enemy_map': map_funcs.create_map(map_funcs.choose_map_size()),
                'self_name': bot_two_name,
                'enemy_name': bot_one_name,
                'bot_memory': copy.deepcopy(bot_memory)}

print('Now, you have to put ships on your map.')

# TODO: uncomment later.
# user_maps = user_ship.put_user_ships_on_map(ships, user_maps)
# map_funcs.display_self_and_enemy_map(user_maps)

bot_one_maps = bot_ship.put_bot_ships_on_map(ships, bot_one_maps)
bot_two_maps = bot_ship.put_bot_ships_on_map(ships, bot_two_maps)
map_funcs.display_self_map(bot_one_maps)
map_funcs.display_self_map(bot_two_maps)

turn = 0

while True:

    bot_one_maps, bot_two_maps = bot_play.play_bot_turn(bot_one_maps, bot_two_maps)
    bot_two_maps, bot_one_maps = bot_play.play_bot_turn(bot_two_maps, bot_one_maps)

    turn = turn + 1
    print('{0}\nTURN: {1}{0}'.format('\n' + '#' * 60, turn))
